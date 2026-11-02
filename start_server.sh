#!/bin/sh
# SPDX-License-Identifier: CC-BY-SA-4.0
set -eu
: "${MODEL_GGUF:?Set MODEL_GGUF to Gemma-2-Ataraxy-9B-Q5_K_M.gguf}"
exec llama-server -m "$MODEL_GGUF" -c 8192 -np 1 -ngl 99 \
  --host 127.0.0.1 --port 8085
