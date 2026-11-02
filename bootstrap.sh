#!/bin/sh
# SPDX-License-Identifier: CC-BY-SA-4.0
set -eu
profile=${1:-all}
if [ "$#" -gt 0 ]; then shift; fi
case "$profile" in ataraxy|hip|all) ;; *) echo 'Usage: sh bootstrap.sh [ataraxy|hip|all]' >&2; exit 2;; esac
PYTHON=${PYTHON:-python3}
"$PYTHON" -c 'import sys; assert sys.version_info >= (3,11), "Use Python 3.11 or later"'
command -v git >/dev/null
"$PYTHON" -m venv .venv-models
if [ "$profile" = ataraxy ]; then
  if command -v uv >/dev/null 2>&1; then
    uv pip install --python .venv-models/bin/python huggingface_hub==0.36.2 cmake==4.1.3
  else
    .venv-models/bin/python -m pip install huggingface_hub==0.36.2 cmake==4.1.3
  fi
else
  if command -v uv >/dev/null 2>&1; then
    uv pip install --python .venv-models/bin/python -r requirements-models.txt
  else
    .venv-models/bin/python -m pip install -r requirements-models.txt
  fi
fi
mkdir -p .tools
if [ ! -d .tools/llama.cpp/.git ]; then
  git init .tools/llama.cpp
  git -C .tools/llama.cpp remote add origin https://github.com/ggml-org/llama.cpp.git
fi
converter=$(.venv-models/bin/python -c 'import json; print(json.load(open("model_versions.json"))["llama_cpp_converter"])')
runtime=$(.venv-models/bin/python -c 'import json; print(json.load(open("model_versions.json"))["llama_cpp_runtime"])')
git -C .tools/llama.cpp fetch --depth 1 origin "$converter"
git -C .tools/llama.cpp checkout --detach "$converter"
.venv-models/bin/python setup_models.py --profile "$profile" --llama-cpp .tools/llama.cpp "$@"
git -C .tools/llama.cpp fetch --depth 1 origin "$runtime"
git -C .tools/llama.cpp checkout --detach "$runtime"
.venv-models/bin/cmake -S .tools/llama.cpp -B .tools/llama.cpp/build -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=OFF
.venv-models/bin/cmake --build .tools/llama.cpp/build --target llama-server --config Release -j "${BUILD_JOBS:-4}"
printf '\nReady. In this terminal set:\nexport LLAMA_SERVER="%s/.tools/llama.cpp/build/bin/llama-server"\n' "$PWD"
.venv-models/bin/python -c 'import json,shlex; [print("export "+k+"="+shlex.quote(v)) for k,v in json.load(open("models/paths.json")).items()]'
