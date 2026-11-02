# Actual public example run / 公开样例实跑

Input: [fictional deployment document](../document.txt). Both released model profiles generated two groups using the pinned configuration. The JSON files include exact prompts, candidates, settings and measured times. Outputs can differ across hardware/backend versions despite fixed seeds.

HIP: 3.33s + 3.73s. Ataraxy: 14.20s + 14.10s (the server also handled another queued job, so these times include waiting). Model loading, installation and human review are excluded.

[Reviewed HIP document](hip-reviewed.txt) and [exact review changes](hip-review-changes.json) show the source-check step. In particular, a candidate changed median to mean; the reviewed copy restores median. Ataraxy candidates retained the pilot quantities and scope on manual comparison; “simpler field labels” should be read against the original “clearer field label” and is restored in the assembled example for precision.

These are implementation examples, not private-case detector scores. No personal text or style corpus is included.

输入为明确标注的虚构 AI 生成部署样例。两套模型均真实运行两组；JSON 包含实际提示词、参数和耗时。HIP 候选曾把 median 改为 mean，核对稿已恢复，修改记录单独提供。此处不将样例输出列为检测成绩。

Optional API fidelity review: [actual three-change patch](api-fidelity-patch.json) and [patched candidate](api-fidelity-candidate.txt), generated from this public synthetic example. See [usage and data flow](../../API_REVIEW.md).
