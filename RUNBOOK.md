[Complete executable guide](QUICKSTART.md) · [完整中文复现步骤](QUICKSTART.zh-CN.md)

# Implementation runbook · 实施流程

## 1. Prepare the environment / 准备环境

Use Python 3.9 or later and a llama.cpp build with `llama-server` available. The runner uses only Python's standard library. The tested configuration was an M3 Pro with 18GB unified memory, one model slot and an 8,192-token context.

Download `Gemma-2-Ataraxy-9B-Q5_K_M.gguf` from [the quantized model repository](https://huggingface.co/bartowski/Gemma-2-Ataraxy-9B-GGUF). The file is approximately 6.65GB. Keep model weights outside the repository; the launch script uses an absolute path.

本项目使用已发布权重，无需训练或模型 API key。实测设备为 M3 Pro、18GB 统一内存；这记录的是已运行环境。模型文件单独下载和存放，不打包上传。

## 2. Prepare private inputs / 准备私人输入

Create `private/` and place your own style sample there as described in [PERSONAL_CORPUS.md](PERSONAL_CORPUS.md). Prepare the new text as TXT or JSONL. For a complete document, use natural paragraph groups of about 100–320 words, retaining each section's reasoning.

```jsonl
{"id":"section-1","text":"The complete original paragraph group goes here."}
{"id":"section-2","text":"The next complete paragraph group goes here."}
```

Keep an untouched original. Preserve headings, tables, code, direct quotations and reference entries for reassembly. Word files can be copied to plain text, or extracted with an existing document converter; the public runner itself accepts TXT/JSONL. Confirm that extraction includes all intended prose and has not mistaken task instructions for the user's text.

保留原稿，分段保持自然完整，不删掉包含数字、引用和条件的句子。标题、表格、代码、引用原文和参考文献保持原样；后续在原文件副本中回填已核对正文。公开脚本处理 TXT／JSONL，Word 回填与排版另行完成。

## 3. Start local inference / 启动本地推理

```sh
export MODEL_GGUF=/absolute/path/Gemma-2-Ataraxy-9B-Q5_K_M.gguf
sh start_server.sh
```

The server listens only on `127.0.0.1:8085`. In a second terminal, from this repository directory:

```sh
python3 rewrite.py private/sections.jsonl runs/voice --style private/my_style.txt
python3 rewrite.py private/sections.jsonl runs/direct
```

Use an empty output directory. Each record produces a numbered TXT and JSON, preserving its ID, source, candidate, exact prompt, parameters, runtime and checks. The voice mode uses the first 2,800 characters of the style file. Direct mode omits this reference.

固定配置为 temperature 0.8、top_p 0.95、top_k 40、min_p 0.05、repeat_penalty 1.05、seed 42、n_predict 1100。每个段落组一轮生成，使用 Gemma 2 模板和 user 消息；不是多轮迭代或微调训练。

## 4. Review and reassemble / 原意核对与回填

Read source and candidate together. Check quantities, units, names, dates, roles, technical definitions, quotations, citations, qualifications, scope and causation. Preserve proposed actions versus completed experiences. Inspect warning fields and output completeness; a numeric spelling change can raise a token warning without changing the value, while a role error can require reading even with no warning.

Correct source mismatches in a separate reviewed copy. Place the checked paragraphs into a copy of the original document. Keep all other material and existing metadata. Render or open the complete result to check headings, tables, page breaks and references.

人工核对是本次实测流程的一部分。先修复原意，再提交检测；不要依据分数保留错义、捏造经历或省略困难内容。生成 JSON 含私人文本，不应随项目上传。

## 5. Compare in GPTZero / Chrome 实测

Use your own logged-in Chrome account. Scan the original and both reviewed complete versions during the same period, with the same mode. Verify the intended input and “Text up-to-date” status. Record date, scan mode, detector version if displayed, actual classification and Human/Mixed/AI probabilities. Also record AI Paraphrased when shown.

Human probability is distinct from Human classification. Keep Uncertain and Mixed outcomes separate. Preserve API or browser errors as missing results rather than scores. The original and candidate should include the same retained headings, tables, references and end matter.

原稿与两份核对稿完整比较；记录概率与实际分类，不将概率写成通过率。仅最终待测文稿需要提交给 GPTZero，本人风格样本无需上传。检测使用你自己的会员或额度。

## 6. Retain a usable result / 保存结果

Choose among content-accurate candidates and keep the original, reviewed output, settings and real detector result. Record which configuration was selected. If neither improves the intended outcome, keep the original. The reported case studies use one-pass generation and source review, not an automatic acceptance rule.

After generation, stop the model server with Ctrl+C to release memory. Keep reusable weights and private originals; publish only the repository's public files and selected non-private results.

## Data flow / 数据流向

| Material | Local inference | GPTZero | Public repository |
|---|---|---|---|
| Personal style sample / 本人语料 | Read as context | Not required | Excluded |
| Source and candidate / 原稿与候选 | Read and generated locally | Sent only when you submit a scan | Excluded |
| Code and prompt / 代码与提示 | Runs locally | Not required | Included |
| Selected cropped evidence / 精选截图 | Captured from a real result | Reflects actual scan | Included after selecting non-private content |

Project-authored materials use CC BY-SA 4.0. See [NOTICE.md](NOTICE.md) for third-party model and interface rights.
