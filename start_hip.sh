#!/bin/sh
# SPDX-License-Identifier: CC-BY-SA-4.0
set -eu
: "${HIP_BASE_GGUF:?Set HIP_BASE_GGUF to Qwen3-4B-Base.Q6_K.gguf}"
: "${HIP_ADAPTER_GGUF:?Set HIP_ADAPTER_GGUF to the matching released HIP adapter GGUF}"
exec "${LLAMA_SERVER:-llama-server}" -m "$HIP_BASE_GGUF" --lora "$HIP_ADAPTER_GGUF" -c 2048 -np 1 -ngl "${GPU_LAYERS:-99}" --host 127.0.0.1 --port 8083
