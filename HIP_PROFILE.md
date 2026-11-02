# HIP comparison profile · HIP 可选配置

A second local profile uses the released Qwen3-4B-Base HIP adapter with independent one-pass candidates and source review. It was tested separately from the default Ataraxy profile, with QuillBot as the initial target of comparison.

第二条本地路线采用已发布的 Qwen3-4B-Base HIP adapter，单轮生成独立候选，再核对原意。本轮先单独验证 QuillBot 的改善，并将相同核对稿提交 GPTZero 对照。

## Full-document results / 全文实测

| Complete document | QuillBot original AI indicator | QuillBot reviewed HIP AI indicator | GPTZero original Human probability | GPTZero reviewed Human probability | Reviewed GPTZero classification |
|---|---:|---:|---:|---:|---|
| C1 · Incident response | 60.06% | 21.31% | 0% | 74% | Human |
| C2 · Stakeholder analysis | 38.37% | 10.95% | 0% | 39% | AI Paraphrased |
| C3 · Healthcare ethics | 58.50% | 4.16% | 0% | 0% | AI Paraphrased |

These are three complete-document comparisons, including retained headings, tables where present, references and end matter. Original and reviewed word counts were 969 → 1,051, 967 → 977, and 788 → 938. GPTZero used Advanced AI Scan, model 4.1o; QuillBot returned v7.1.0. QuillBot's AI indicator and GPTZero's Human probability have different definitions. C2's GPTZero probabilities were AI 61%, Mixed 0%, Human 39%; its classification remains AI Paraphrased.

三篇全文在 QuillBot 上均有改善。表中采用最终核对版本；C1 在最后一次措辞修订前也检测过，最终稿已重新实测。数字表示各平台原生指标，不换算为通过率。结果来自三篇完整文稿与三个段落组的探索测试，后续文稿继续逐篇核对和比较。

The [native result table](evidence/hip_profile_results.csv) contains all 29 valid scans from the initial follow-up and the third-document extension, plus two missing repeat attempts, including paragraph comparisons and intermediate complete-document versions. It records each scope and version separately. The earlier [cross-detector results](CROSS_DETECTOR.md) concern Ataraxy candidates and remain a separate comparison.

## Exact local configuration / 本地配置

Base: [Qwen/Qwen3-4B-Base](https://huggingface.co/Qwen/Qwen3-4B-Base), using [mradermacher's Q6_K GGUF](https://huggingface.co/mradermacher/Qwen3-4B-Base-GGUF). Adapter: [YixuanEvenXu/Qwen3-4B-Base-HIP-adapter](https://huggingface.co/YixuanEvenXu/Qwen3-4B-Base-HIP-adapter), converted to F16 GGUF with llama.cpp's `convert_lora_to_gguf.py`. Match the Base model exactly; the Instruct model is a different base.

The tested runtime was llama.cpp with Metal, one slot and a 2,048-token context on an M3 Pro with 18GB unified memory. Sampling: temperature 1.0, top_p 0.95, top_k 50, min_p 0, repeat_penalty 1, seed 42, up to 800 generated tokens, stopping at `</target_text>`. Use HIP's source/target format, without a chat template or system message.

```text
<source_text>
Complete original paragraph group
</source_text>

<target_text>
```

The full documents use this unseeded target opening. C2 used seed 43 for two groups after seed-42 candidates changed the source meaning. C3 used seed 43 for two groups after content review. A separate paragraph experiment used the opening `The company` on C1. These are independent candidates from the original, not successive rewrites of an earlier output.

## Run / 运行

Download the Base GGUF and adapter separately. Convert the released adapter directory with a compatible llama.cpp checkout and its conversion dependencies:

```sh
python3 /path/to/llama.cpp/convert_lora_to_gguf.py \
  --base-model-id Qwen/Qwen3-4B-Base --outtype f16 \
  --outfile /path/to/hip-adapter-f16.gguf /path/to/released-hip-adapter
```

Stop another local model server to release memory before loading this profile.

```sh
export HIP_BASE_GGUF=/absolute/path/Qwen3-4B-Base.Q6_K.gguf
export HIP_ADAPTER_GGUF=/absolute/path/hip-adapter-f16.gguf
sh start_hip.sh
```

In another terminal, use TXT for one complete paragraph group of at most 320 words, or JSONL for multiple groups:

```sh
python3 hip_rewrite.py private/sections.jsonl runs/hip
```

Each JSONL record contains `id` and `text`. Optional `seed` selects a particular independent candidate; optional `lead` supplies a target opening. Save each run in a new directory. TXT and JSON output retain the source, candidate, prompt, settings, timing and warnings.

```jsonl
{"id":"section-1","text":"Complete original paragraph group.","seed":42}
{"id":"section-2","text":"Another complete paragraph group.","seed":43}
```

Review quantities, units, named entities, roles, citations, qualifications and causal relationships before testing. Reject candidates that reverse or materially reconstruct claims. This experiment repaired source mismatches in separate reviewed copies, including notification deadlines, hypothetical wording, authority and contract restrictions. The table measures this generation-plus-review workflow.

本轮收益对应“生成＋内容核对”的组合流程。先核对事实，再比较检测结果；不要直接把原始输出当作最终稿。固定参数方便重跑，Metal 后端仍可能产生不同候选；批量入口复测时，两组中一组逐字复现，另一组输出不同，因此每次运行都需要重新核对。

The initial two-document follow-up used nineteen local generation calls, including the two-record batch-entry check, taking 150.21 seconds in total. The third-document extension used fourteen additional generations, detailed in [the combination comparison](COMBINATIONS.md). Review and browser time were not timed. There was no external generation API charge, GPU purchase or additional detector-credit purchase. Scans used the existing logged-in Chrome session and memberships.

## Sources / 来源

The model and trained prompt format come from [HIP](https://github.com/YixuanEvenXu/humanization-by-iterative-paraphrasing). A [forum experiment](https://www.reddit.com/r/SideProject/comments/1x0eog6/i_spent_a_week_taking_apart_ai_detectors_with/) and its [implementation](https://github.com/ervin-mo/humanizar-es) motivated testing independent first-pass candidates and alternative openings; their reported scores are separate from the measurements above. Our runner reuses the existing local HIP deployment and does not include their code or any forum writing corpus.

## Model combinations / 模型组合

See [the complete model-order comparison](COMBINATIONS.md) for HIP, Ataraxy → HIP and HIP → Ataraxy on the third document.
