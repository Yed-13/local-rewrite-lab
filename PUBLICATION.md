# Publication routes / 发表方向

## Recommended practical-publication routes / 技术短文优先方向

**First choice: HackerNoon. Second choice: Towards AI.** Both provide editorial review for technology/practitioner articles, which fits a concise account of a working open-source tool and measured observations. For direct publication to the model-using community, Hugging Face is a complementary route. This prioritizes readership and editorial selection rather than journal indexing.

**首选 HackerNoon，其次 Towards AI。** 两者都接受实践类技术文章并有编辑审核，适合介绍可运行的开源工具、方法与真实观察。Hugging Face 可作为直接面向模型使用者的补充渠道；选择重点是读者与编辑认可，不以学术索引为目标。

| Platform | Publication type | How this project fits / next step |
|---|---|---|
| [HackerNoon](https://help.hackernoon.com/more-faqs) | Editor-reviewed technology publication | Prepare a practical article with the implementation, one public example and paired results. Submit through the writing editor for editorial consideration. Ordinary contributor selection is based on the story, not payment; branded-author products are separate. |
| [Towards AI](https://towardsai.com/contribute/) | Editor-reviewed AI publication on Medium | Welcomes implementation, evaluation and accounts of practitioners' own work. Submit an unpublished Medium draft. Guidance targets roughly 850+ words / five minutes, with exceptions for strong shorter pieces. |
| [Hugging Face Blog Articles](https://huggingface.co/docs/hub/blog-articles) | Community technical article | Strong audience fit for a released model-based tool. A personal article requires a confirmed email plus PRO or eligible Team/Enterprise membership. Community publication does not imply editorial acceptance or peer review. |
| [DEV](https://dev.to/help/writing-editing-scheduling) | Developer community post | A direct Markdown tutorial and repository introduction; supports canonical links when cross-posting. |
| [Computational Linguistics: Squibs and Discussions](https://cljournal.org/submissions.html) | Peer-reviewed academic journal | At most 8 content pages plus references; no processing/publication charges. Requires unexpectedness, genuine novelty or wide readership interest. A short format still requires a substantive NLP contribution; not the first target for a practical tool introduction. |

Platform-specific AI-writing, attribution, prior-publication and promotional-content rules apply when preparing a submission. Towards AI explicitly distinguishes writing assistance from generated article text; check its current contributor page when finalizing the manuscript. No article has been submitted or published on the user's behalf by this repository update.

投稿前按所选平台核对原创性、AI 写作、首发和推广内容规定。当前未代为注册、投稿或发布文章。

## Suggested angle / 建议角度

**Working title:** *Same Text, Different Verdicts: What Local Rewriting Reveals About AI Detectors*.

Lead with the observed disagreement between detectors, then show the local pipeline, a public example and source-fidelity corrections. A concise 900–1,200-word technical piece is a practical target for this project, not a universal platform rule. The project combines released models and a review workflow; it does not introduce a newly trained rewriting model or a universal detector bypass.

建议从“同一文本为何在不同检测器上得到不同结论”切入，再展示本地流程、公开样例和原意核对。篇幅可控制在 900–1,200 英文词，这只是本项目的编辑建议。

## Optional academic routes / 可选学术方向

[ARR / ACL](https://aclrollingreview.org/cfp) accepts four-page short conference papers with a required Limitations section. [ACL 2027](https://2027.aclweb.org/calls/main/) lists January 4, 2027 AoE for its ARR deadline; review-service eligibility rules apply. This becomes relevant after a broader controlled study, rather than as the immediate practical-publication route.

[JOSS](https://joss.readthedocs.io/en/latest/submitting.html) is not the present target: it requires substantial research software, sustained public development and an OSI-approved software license. Current CC BY-SA project licensing is retained. [Zenodo](https://help.zenodo.org/docs/get-started/quickstart/) and arXiv provide archiving/preprint routes, not journal editorial acceptance.

## Evidence to develop / 学术稿需要补充的实验

Keep the fixed configuration and review corrections separate from detector-driven selection. Expand beyond the current three private document cases using openly licensed or explicitly synthetic public texts, multiple domains and a held-out evaluation set. A practical next study could use 20–30 independent documents; that is a proposed study size, not a venue requirement. Publish runnable public inputs and outputs, native detector results, and the factual corrections required by each method. Paragraph groups from one document should not be counted as independent full-document cases.

下一步用公开可再分发文本增加独立文章数量，固定配置后留出测试集，同时记录模型原始输出与人工核对稿。建议的 20–30 篇是研究设计建议，不是期刊规定。现有私人原文、个人语料和登录信息继续保留本地。

## Official sources / 官方信息

[ACL 2027 call](https://2027.aclweb.org/calls/main/) · [ARR call and format](https://aclrollingreview.org/cfp) · [CL submission categories and fees](https://cljournal.org/submissions.html) · [JOSS submission criteria](https://joss.readthedocs.io/en/latest/submitting.html) · [JOSS review criteria](https://joss.readthedocs.io/en/latest/review_criteria.html) · [Hugging Face blog publishing](https://huggingface.co/docs/hub/blog-articles) · [DEV writing help](https://dev.to/help/writing-editing-scheduling) · [Zenodo quickstart](https://help.zenodo.org/docs/get-started/quickstart/)

No manuscript or technical article has been submitted through this repository update. / 本次仓库更新尚未代为投稿或发布短文。
