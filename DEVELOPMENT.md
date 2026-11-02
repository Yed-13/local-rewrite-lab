# Development track · 开发记录

Updated November 2, 2026.

The released workflow emerged from several experimental stages: local deployment, personal-writing experiments, model and prompt comparisons, source-fidelity review, and cross-document evaluation. These stages informed the current one-pass Ataraxy configuration.

公开流程经过本地部署、个人写作参考实验、模型与提示对比、原意核对及跨文档测试等阶段逐步形成。当前版本采用一轮 Ataraxy 候选生成、内容核对和真实检测。

## November 1, 2026 / Local deployment

Deployed HIP with the released Qwen3-4B-Base adapter and the dedicated 12B humanizer locally on an M3 Pro with 18GB unified memory. Completed paragraph-level inference, including HIP rounds 1–3, and compared content retention. The later released configuration uses a different 9B model.

在本机部署 HIP 与 12B humanizer，完成单段、批量及多轮推理，比较数字、术语、条件和论点保留情况。

## November 2, 2026 / Personal writing and model comparisons

Compared own-writing context, small-adapter experiments, checked rewrite pairs, and several model/prompt routes. Selected Gemma-2-Ataraxy-9B Q5_K_M plus source review for the public runner. The selected runner uses an existing model; the writer's prose is supplied as prompt context.

对比个人旧作参考、小型适配器实验、经核对的改写配对以及不同模型和提示路线。公开入口使用已有 Ataraxy 权重，个人语料仅作运行时风格参考。

## November 2, 2026 / Cross-document evaluation

Applied two fixed one-pass configurations to three additional complete documents from different subjects. Reviewed source fidelity before testing complete texts in GPTZero. Original and reviewed results are preserved in [the evaluation record](EVALUATION.md).

对不同主题的完整文稿进行固定配置迁移测试，先核对原意，再比较全文检测结果。

## November 2, 2026 / Cross-detector checks

Extended the same previously reviewed texts to additional detector interfaces, without rewriting them for the new detectors. Full-document and matched-paragraph results are tracked separately. See [cross-detector replication](CROSS_DETECTOR.md) for measured outcomes and access conditions.

将同一批已核对文本扩展到其他检测器，分别记录全文与对应完整段落的结果，不根据新检测器的分数继续改写。
