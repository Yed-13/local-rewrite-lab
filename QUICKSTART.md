# Reproduce the workflow

[简体中文](QUICKSTART.zh-CN.md) · [Overview](README.md) · [Fixed versions](model_versions.json)

## 1. Requirements and model choice

Install Git, Python 3.11 or newer and the Xcode command-line tools (`xcode-select --install` on macOS). Allow approximately 20GB free disk for both profiles, dependencies and build files; existing Hugging Face caches are reused. Run one model server at a time when memory is limited.

| Profile | Released weights used | Local file size |
|---|---|---:|
| Ataraxy | Gemma-2-Ataraxy-9B Q5_K_M | 6.65GB |
| HIP | Qwen3-4B-Base Q6_K + matched HIP f16 LoRA | 3.31GB + 0.53GB |

HIP preparation also caches the approximately 1.06GB published adapter before conversion. `model_versions.json` pins the model revisions, runtime and converter separately. The converter used to prepare the adapter differs from the tested runtime. No training is required. Third-party model licenses remain applicable.

```sh
git clone https://github.com/Yed-13/local-rewrite-lab.git
cd local-rewrite-lab
PYTHON=python3.11 sh bootstrap.sh all
```

Use your installed Python executable in place of `python3.11`. Choose `ataraxy` or `hip` instead of `all` to install one profile. The script creates `.venv-models`, downloads weights through the Hugging Face cache, converts the HIP adapter, and builds the pinned `llama-server`. Copy the export commands printed at the end into your terminal. Alternatively:

```sh
export LLAMA_SERVER="$PWD/.tools/llama.cpp/build/bin/llama-server"
export MODEL_GGUF="$PWD/models/Gemma-2-Ataraxy-9B-Q5_K_M.gguf"
export HIP_BASE_GGUF="$PWD/models/Qwen3-4B-Base.Q6_K.gguf"
export HIP_ADAPTER_GGUF="$PWD/models/hip-adapter-f16.gguf"
```

Existing GGUF files can be reused without a second copy:

```sh
PYTHON=python3.11 sh bootstrap.sh all   --reuse-ataraxy /absolute/path/Gemma-2-Ataraxy-9B-Q5_K_M.gguf   --reuse-hip-base /absolute/path/Qwen3-4B-Base.Q6_K.gguf   --reuse-hip-adapter /absolute/path/hip-adapter-f16.gguf
```

Omit the last flag to convert the published adapter yourself. For cached, disconnected model preparation, run `.venv-models/bin/python setup_models.py --profile all --llama-cpp .tools/llama.cpp --offline`; the complete bootstrap still needs source/dependency access. Linux CPU is available through `GPU_LAYERS=0`; Linux GPU backend configuration is not validated by this bootstrap.

## 2. Prepare a document

Export document body text as UTF-8 TXT, with blank lines between natural paragraphs. DOCX formatting is not reconstructed by this TXT workflow. Preserve your original file separately.

```sh
python3 workflow.py prepare examples/document.txt runs/demo/job
```

This writes `document.json` (the reassembly plan) and `sections.jsonl` (model input). Adjacent prose paragraphs are grouped up to 320 words; paragraphs are never cut in half. A longer paragraph requires a natural sentence-boundary split. Headings, Markdown tables, block quotations, code fences and reference end matter are retained. Inspect the plan before generation, especially short prose that resembles a heading. For plain-text quotations or unusual end-matter headings, edit the source layout or prepare explicit JSONL records instead.

The bundled example is fictional, AI-generated deployment material. It contains quantities, a median, conditions and an explicit evidence limitation. Its outputs demonstrate the implementation; they are separate from the private evaluation cases.

## 3. Generate candidates

In terminal A, start one model and wait until it is listening:

```sh
sh start_hip.sh
```

In terminal B, from the same repository:

```sh
python3 hip_rewrite.py runs/demo/job/sections.jsonl runs/demo/hip
```

Stop terminal A with Ctrl-C before starting Ataraxy. To compare a direct one-pass candidate:

```sh
sh start_server.sh
```

Then, in terminal B:

```sh
python3 rewrite.py runs/demo/job/sections.jsonl runs/demo/ataraxy
```

Ataraxy optional personal style context: add `--style private/my_style.txt`. The first 2,800 characters are used. Direct mode and HIP require no personal corpus. [Preparing your own sample](PERSONAL_CORPUS.md).

Each numbered JSON stores the source, exact formatted prompt, generation settings, runtime and warnings; the matching TXT contains the candidate. Ataraxy asks the server to apply the model chat template and verifies Gemma turn delimiters. HIP uses the published source/target completion format, not an instruction-chat template. Parameters are fixed in the runners; see [HIP profile](HIP_PROFILE.md) and [runbook](RUNBOOK.md).

## 4. Review and rebuild

```sh
python3 workflow.py review runs/demo/hip runs/demo/hip-reviewed
```

Read `comparison.md` and edit the numbered TXT copies. Check numbers and units, mean versus median, names, terminology, citation claims, causal language, conditions, and omitted or added facts. Digit-token warnings are prompts to review: spelling a number as a word can trigger them, while changing “median” to “mean” can escape them. Review against the original, not just the previous model output.

```sh
python3 workflow.py assemble runs/demo/job/document.json   runs/demo/hip-reviewed runs/demo/final-hip.txt
```

The assembler restores retained source blocks and refuses to overwrite an existing output. Use new directory names for later runs. [Worked public example](examples/expected/README.md) includes actual raw outputs, reviewed text and corrections.

## 5. Optional selective second stage

The tested selective configuration starts with reviewed HIP prose and sends only the last two rewrite groups to Ataraxy. Keep the remaining HIP groups unchanged. This is an experimental configuration; [paired results](SELECTIVE_REWRITE.md) show transfer performance.

With the Ataraxy server running:

```sh
python3 workflow.py tail runs/demo/job/document.json   runs/demo/hip-reviewed runs/demo/tail.jsonl --groups 2
python3 rewrite.py runs/demo/tail.jsonl runs/demo/tail-ataraxy
python3 workflow.py review runs/demo/tail-ataraxy runs/demo/tail-reviewed   --original-plan runs/demo/job/document.json
```

After reviewing the new copies against the original:

```sh
python3 workflow.py assemble runs/demo/job/document.json   runs/demo/hip-reviewed runs/demo/final-selective.txt   --overlay runs/demo/tail-reviewed
```

The small public example has only two groups, so selecting two rewrites its entire body. Use a longer document to exercise partial replacement.

## 6. Compare actual detector results

Use the same complete original and final text, account and scan mode within a short testing window. GPTZero Advanced: paste a text, run a fresh scan, record the displayed classification and separate AI/Mixed/Human probabilities, plus AI Paraphrased if displayed. Repeat on QuillBot and Originality using their native displayed score and label. Online submission sends that text to the selected service; it does not need your style corpus.

Copy `examples/detector_results.csv` to a local run directory and add one row per service and text version. Record scan time, model version, words, native score, classification and cost. Leave unavailable fields blank and mark failed or quota-blocked scans separately. Human classification count and mean Human probability measure different things. Do not translate another service's AI score into GPTZero Human probability.

Browser automation tied to a logged-in personal session is not bundled. These manual steps use the same visible scan controls and avoid requiring an API plan. No paid detector API or detector credentials are needed for local inference.

## Troubleshooting

| Symptom | Action |
|---|---|
| Python version error | Set `PYTHON` to a Python 3.11+ executable. |
| HTTP 503 | Wait for model loading to finish; confirm the server log says listening. |
| Port already occupied | Stop the earlier model server; HIP uses 8083 and Ataraxy 8085. |
| Insufficient memory | Run only one server, close memory-heavy apps, reduce `GPU_LAYERS` or use a smaller compatible quantization and record the change. |
| Unexpected template | Check the exact Ataraxy model; do not substitute a different family silently. |
| HIP output looks like instructions | Confirm the Base model and matched adapter, and use `hip_rewrite.py`. |
| Output limit/truncation warning | Shorten the input group naturally and rerun into a new directory; review for omissions. |
| Download interrupted | Rerun; Hugging Face caching is reused. Do not delete shared model caches. |

Validation: a fresh isolated dependency environment and the pinned runtime build completed using existing weight files. Both profiles performed real batch inference; HIP adapter conversion and document review/reassembly were also exercised. Existing cache reuse was tested; a second multi-gigabyte fresh download was unnecessary.
