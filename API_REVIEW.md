# Optional API source-fidelity review / 可选 API 原意校核

[English / 简体中文](#使用方法)

Use `fidelity_patch.py` after local generation to propose narrowly scoped source corrections. It compares the original and candidate, requests exact text replacements, and saves a patched candidate for review. The local-only workflow remains available without this step.

**Data flow:** this optional step sends the original and candidate to OpenAI. It does not send your personal style corpus. API usage is billed separately. Set `OPENAI_API_KEY` in your local environment before running.

```sh
python3 fidelity_patch.py private/source.txt runs/candidate.txt runs/fidelity-review \
  --model gpt-6-astra --output-tokens 2000 --max-cost 0.25
```

The output directory must be new. It contains `response.json` (source, candidate, model, usage and estimated cost), `patch.json` (changes and unresolved points) and `candidate.txt`. Read the patch and compare the result with the source before using it. The tool rejects ambiguous or overlapping replacement spans and incomplete responses. It does not overwrite the input files.

`--max-cost` limits a conservative request estimate using fixed standard token rates. It is not an account-wide spending limit. The response records actual token usage and a cost estimate without cache discounts. Check [OpenAI pricing](https://developers.openai.com/api/docs/pricing) when rates change.

The public [synthetic pilot example](examples/document.txt) was run through GPT-6 Astra. It proposed three corrections: restore the pilot comparison wording, change **mean** back to **median**, and restore the missed accessibility field. [Actual patch](examples/expected/api-fidelity-patch.json) · [Patched candidate](examples/expected/api-fidelity-candidate.txt). The returned usage implied approximately **$0.01669** at the recorded standard rates. These examples demonstrate fidelity review, not detector performance.

## 使用方法

`fidelity_patch.py` 用于本地生成后的原意校核。它将原文和候选发送到 OpenAI，返回可逐条检查的精确文本替换，不上传个人风格语料。纯本地流程可以省略此步骤。先在本机环境配置 `OPENAI_API_KEY`，再运行上面的命令。

结果目录保存输入、模型、用量、费用估算、补丁和修订候选。原文与输入候选不会覆盖。使用前仍需对照原文核对，特别检查数字、术语、引文对应关系、条件和结论强度。工具会拒绝重复匹配、相互重叠的替换及未完整生成的响应。

公开虚构样例实际修复了比较过程、mean/median 和漏填字段三处表述，用量对应费用约 0.01669 美元。这里展示的是原意校核功能，不是检测成绩。
