# Selective second-stage rewriting / 选择性二次改写

**Configuration:** reviewed HIP prose → Ataraxy on the last two natural rewrite groups only → review against the original → restore retained headings and end matter. Use the fixed model versions and runner parameters in this repository. [Executable steps](QUICKSTART.md#5-optional-selective-second-stage).

固定规则：先核对 HIP 全文，只将末尾两组送入 Ataraxy，再对照原文核对；其余正文及原有标题、表格、参考文献保留。

## Complete-document comparisons / 全文比较

| Case | Version | GPTZero Human probability ↑ | QuillBot AI ↓ | Originality AI ↓ | Originality label |
|---|---|---:|---:|---:|---|
| C1 | Original | 0% | 60.06% | 90% | AI |
| C1 | HIP | 74% | 21.31% | 90% | AI |
| C1 | Selective last two groups | **82%** | 24.25% | **65%** | **Mixed** |
| C2 | Original | 0% | 38.37% | 94% | AI |
| C2 | HIP | 39% | **10.95%** | 90% | AI |
| C2 | Selective last two groups | 0% | 24.20% | 88% | AI |
| C3 | Original | 0% | 58.50% | 90% | AI |
| C3 | HIP | 0% | **4.16%** | 65% | Mixed |
| C3 | Selective summary group | 69% | 4.20% | 70% | Mixed |
| C3 | Selective last two groups | **82%** | 11.77% | **65%** | Mixed |

GPTZero Advanced, model 4.1o; QuillBot native AI indicator; Originality 5.0. All comparisons use complete texts including retained end matter. Baseline rows carry forward the exact stored versions from the preceding phase; selective candidates were scanned in the subsequent same-session testing window. Values are native service outputs, not interchangeable probabilities. [CSV](evidence/selective_results.csv).

## Selection and transfer / 选择与迁移

Two C3 mixtures were fixed before their scans: replace the summary group only, or replace the last two groups. Both used previously reviewed second-stage outputs. After those results, the last-two-group rule was frozen and transferred to C1 and C2 without changing sampling parameters or selecting additional combinations from their scores. C1/C2 each required two new local generation calls.

For the three last-two-group versions, GPTZero classified **2 Human, 0 Mixed, 1 AI Paraphrased** out of three valid complete documents. Human probabilities were 82%, 0%, 82%; the Human-classified proportion was 2/3. Originality classified **2 Mixed and 1 AI**, with no Human/Original result. These are three private document cases; their full text remains local. Public synthetic fixtures reproduce the implementation, while this table reports those private-case measurements.

固定末尾两组规则在三篇上得到 GPTZero 两篇 Human、一篇 AI Paraphrased；Originality 两篇 Mixed、一篇 AI。QuillBot 三篇均比单独 HIP 的 AI 指标高。C2 未显示稳定迁移，因此当前保留分目标配置：QuillBot 优先 HIP；GPTZero 与 Originality 联合探索可试选择性二次改写，仍需逐稿核对与检测。

## Fidelity and runtime / 原意与耗时

The four new transfer groups all needed source corrections before scanning. Review restored a clean-backup condition, corrected incident-review wording and assignment scope, restored stakeholder-register and product-configuration terms, separated Sue from the office manager, restored the website partner, changed an overstrong obligation back to a recommendation, and reinstated the omitted customer-service conclusion. Reviewed outputs were checked again against their source groups. C3 used the previously reviewed group versions without new editing.

| New transfer generation | Groups | Groups needing correction | Measured request time |
|---|---:|---:|---:|
| C1 | 2 | 2 | 26.56s |
| C2 | 2 | 2 | 20.69s |
| C3 mixtures | 0 new calls | Previously reviewed | Reassembly only |

Times exclude loading, manual review and detector latency; the server also handled a small public-example job, so request durations can include queue time. The phase completed **12 valid full-document scans** (four candidates × three detectors). Originality used **41 existing free credits**; new API purchases and new cash spend were **$0**. No automatic faithfulness guarantee or universal detector configuration emerged from these results.

原意核对发现的具体错误会影响选稿，不能省略。局部二次改写改善了部分全文判断，但并非在每个平台、每篇文本上同时优于 HIP。
