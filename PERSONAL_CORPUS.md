# Personal corpus preparation · 本人语料准备

## Actual reference size / 实际使用量

The tested own-style configuration used the first **2,800 characters**, approximately **467 English words**, from one older self-authored piece. The local model reads this as prompt context. No new model training is performed.

本次有效配置实际取本人旧作的前 **2800 字符，约 467 个英文词**，作为提示中的风格参考。历史写作语料库用于挑选合适片段，并非全部送入模型，也不需要把整个语料库打包发布。

## Prepare one suitable piece / 准备一篇合适旧作

Start with one English piece of roughly 500–1,000 words whose authorship you can confirm. Prefer analytical prose for an analytical document, or reflective prose for a reflection. Remove personal identifiers, editorial annotations, task instructions, references and long quotations. Keep complete prose that shows your vocabulary, sentence habits and transitions.

先准备一篇约 500–1000 词、你确认是自己写的英文旧作。尽量与目标稿件文体相近，保留能体现用词、句式与过渡方式的正文。去掉身份信息、老师批注、题目说明、参考文献和大段他人引文。保存为 UTF-8 纯文本。

Place the selected passage at the beginning of `private/my_style.txt`. The runner uses only the first 2,800 characters, so a longer archive does not automatically provide more context. There is no experimentally established minimum sample size or measured benefit from using a larger archive in this configuration.

把选好的片段放在 `private/my_style.txt` 开头。脚本只取前 2800 字符；放入更多文件不会自动增加输入量。本次未测最小词数门槛，也未验证更大语料库的额外收益。

## Keep private material local / 私人材料只留本地

```text
local-rewrite-lab/
├── rewrite.py
├── private/                 # ignored by Git
│   ├── my_style.txt         # your own writing
│   └── sections.jsonl       # the text to rewrite
└── runs/                    # ignored by Git
    ├── voice/
    └── direct/
```

Both `private/` and `runs/` are ignored. Generated JSON includes the input and full prompt, including the personal style passage, so run outputs belong in the private local workspace as well. Share only the code and explicitly selected public results.

`private/` 与 `runs/` 都已加入忽略规则。输出 JSON 含原文及完整提示，提示内也含个人风格片段，因此运行结果同样应留在本地。公开包不包含本人语料或文稿全文。

The current workflow has no Reddit or forum-corpus dependency. Public availability does not establish a post's authorship or redistribution license; no scraped forum text is bundled as a validated ingredient.

当前有效流程不依赖 Reddit 或论坛语料，因此没有附带论坛抓取文本。直接改写模式无需本人语料：省略 `--style` 即可。
