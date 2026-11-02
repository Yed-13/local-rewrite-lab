# Model order comparison · 模型顺序对照

The third complete-document test compares the same healthcare-ethics text using one model and two model orders. Both stages use the configurations in the [Ataraxy runbook](RUNBOOK.md) and [HIP profile](HIP_PROFILE.md). Read the output against the original before adopting a stage; retained headings, references and other end matter are the same throughout.

第三篇全文比较单模型与两种模型顺序。各阶段采用已有固定参数，先对照原稿核对，再提交检测；标题、参考文献及其他保留内容相同。

## Complete-document measurements / 全文测量

| Workflow | QuillBot AI indicator | GPTZero AI probability | GPTZero Mixed probability | GPTZero Human probability | GPTZero classification |
|---|---:|---:|---:|---:|---|
| Original | 58.50% | 100% | 0% | 0% | AI |
| Ataraxy | 63.55% | 10% | 0% | 90% | Human |
| HIP | 4.16% | 100% | 0% | 0% | AI Paraphrased |
| Ataraxy → HIP, with one retained first-stage group | 3.05% | 82% | 18% | 0% | AI Paraphrased |
| HIP → Ataraxy | 64.89% | 2% | 0% | 98% | Human |

QuillBot returned v7.1.0; GPTZero used model 4.1o, Advanced AI Scan. The original contained 788 words; the three newly reviewed variants contained 938, 885 and 786 words. Ataraxy's QuillBot baseline is the previously verified 63.55% result for the same stored text. Two attempts to repeat that exact baseline produced no fresh response and are recorded as missing scans. The other rows were measured in this extension.

On this document, ending with HIP favored the QuillBot result, while ending with Ataraxy favored GPTZero. The 1.11-point QuillBot difference between HIP and Ataraxy → HIP provides little practical reason to add the second model as a default. Keep single-pass HIP for the QuillBot profile; retain Ataraxy for GPTZero and the reverse combination as an optional comparison.

本篇中，以 HIP 结束的路线降低了 QuillBot 指标；以 Ataraxy 结束的路线获得 GPTZero Human 分类。双模型相对单轮 HIP 在 QuillBot 只多降低 1.11 个百分点，默认流程继续保持单模型简洁，组合入口供逐篇比较。

The opening group in Ataraxy → HIP retains its reviewed Ataraxy input after neither HIP candidate preserved attribution and quantities. It is a guarded fallback, not an adopted second-stage rewrite. Other groups were checked for consent conditions, contractual limits, chronology, citations, the author's position and proposed requirements versus existing facts. Exact corrections and private text remain local.

Ataraxy → HIP 的开头段组保留了已核对的第一阶段文本。其他段组核对了条件、合同范围、时间、引用、作者立场，以及建议与既有事实的区别。

## Run the comparisons / 重跑方式

Start the first model using its documented launch command, generate candidates, then save reviewed groups as a new private JSONL file. Stop that server to release memory before loading the second model.

```sh
# Ataraxy → HIP
python3 rewrite.py private/sections.jsonl runs/ataraxy-stage
# Review against the original and save private/reviewed-ataraxy.jsonl.
# Switch from start_server.sh to start_hip.sh.
python3 hip_rewrite.py private/reviewed-ataraxy.jsonl runs/ataraxy-hip
```

```sh
# HIP → Ataraxy
python3 hip_rewrite.py private/sections.jsonl runs/hip-stage
# Review against the original and save private/reviewed-hip.jsonl.
# Switch from start_hip.sh to start_server.sh.
python3 rewrite.py private/reviewed-hip.jsonl runs/hip-ataraxy
```

Use new output directories. Keep the original alongside both stages; the final review compares with the original, not just the intermediate. HIP used seed 43 for two content-fidelity retries in the single-model route, and one retry in the Ataraxy → HIP route; other new generations used seed 42. HIP's first group reused the previously reviewed candidate. No personal style reference was added in these comparisons.

This extension generated 14 candidates in 190.82 seconds and completed nine fresh detector scans. The [native data](evidence/hip_profile_results.csv) records the missing repeats separately and also retains the earlier profile measurements. No extra API, GPU or detector purchase was made. Review and browser time are additional and were not timed.
