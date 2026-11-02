# Publication routes / 发表方向

## Primary goal: Google Scholar discovery / 主目标：Google Scholar 检索

**Recommended order: a short research report → one suitable preprint server → a separate practitioner article.** Google Scholar covers technical reports and preprints as well as journal papers. Individual indexing must be checked after publication; depositing a document, receiving a DOI or adding it manually to a Scholar profile does not establish that Scholar has indexed it. [Google Scholar inclusion guidance](https://scholar.google.com/intl/en/scholar/inclusion.html).

**建议顺序：短研究报告 → 选择一个预印本平台 → 单独的媒体解读。** 先形成可被学术搜索发现的完整报告，再用媒体文章传播项目。Google Scholar 收录范围包含技术报告和预印本，并不要求先发表期刊。发布后需要实际检索确认，不能将 DOI 或手动添加的个人资料条目当成收录证明。

| Priority | Route | Review and discovery | Project-specific decision |
|---|---|---|---|
| 1 | [arXiv](https://info.arxiv.org/help/submit/index.html) | Scholarly preprint with moderation, not journal peer review; a standard route for scholarly discovery | First candidate for an NLP evaluation report. Prepare the complete report, check the appropriate category, and resolve any [first-submission endorsement](https://info.arxiv.org/help/endorsement.html). Endorsement is separate from content acceptance. |
| 2 | [Preprints.org](https://www.preprints.org/instructions-for-authors) | Screened preprint, not peer-reviewed; the platform [reports Google Scholar indexing](https://www.preprints.org/news/post/preprints-org-celebrates-announcement-of-its-40000th-preprint) | Practical alternative: Technical Note, Brief Report and Short Note are supported. [Posting is free and the manuscript uses CC BY 4.0](https://www.preprints.org/about). Check manuscript-license compatibility before submission; the repository's CC BY-SA license is unchanged. |
| Later | [Computational Linguistics: Squibs and Discussions](https://cljournal.org/submissions.html) | Formal academic peer review; up to 8 content pages, no processing/publication charges | Consider after establishing a novel, focused result with broader evaluation. It is not the lightweight entry route. |
| Archive only | [Zenodo](https://support.zenodo.org/help/en-gb/18-general/61-is-zenodo-indexed-by-google-scholar) | Code/data archiving and DOI | Zenodo currently states that Google Scholar does not index its records. Use for archiving if needed, not as the Scholar strategy. |

Preprints.org accepts computer science research, but generally excludes coursework: the proposed submission is a new report about the rewriting experiments, not a relabeled private source document. Its stated Scholar coverage is platform-level evidence; acceptance and indexing of this particular report are still future checks. Avoid depositing identical manuscripts on multiple preprint servers just to multiply records; Preprints.org recommends one version history.

Preprints.org 接受计算机科学研究及技术短报告，通常不接受课程作业。拟投稿的是关于改写实验的新研究报告，不是把私人原文换标题上传。它已公布平台层面的 Scholar 收录记录，具体报告仍需通过筛选并在上线后核验检索。优先维护一个预印本版本记录，不为增加条目而重复投放。

## Concrete preparation sequence / 实施顺序

1. **Research report:** prepare approximately 4–6 pages plus references as a project target, not a venue requirement. Explain the research question, released models, fixed prompts, source-fidelity review, native detector metrics and complete aggregate results. Suggested title: *Source-Preserving Local Rewriting Across AI Detectors: A Small-Scale Evaluation*.
2. **Public evaluation material:** add openly redistributable or explicitly synthetic texts; keep private manuscripts and personal writing samples local. A proposed next benchmark of 20–30 independent documents would improve the basis for a research submission. Fix configuration choices before a held-out comparison. Do not count groups from one document as independent document cases.
3. **Submission package:** finalize the manuscript, references, public input/output examples, scripts and results table. Confirm author names, affiliations, contact details and manuscript license with the author before actual submission. Choose the appropriate preprint category; author account/endorsement status has not been checked.
4. **Canonical posting:** try arXiv after content and eligibility preparation; use Preprints.org as an alternative when suitable, rather than automatically posting the same version to both. Any content-scope rejection should be addressed before changing hosts. Publication fees or optional purchases require approval first.
5. **Discovery check:** after the report is public, search Google Scholar for the exact title and author, confirm the matching document and version, then record the real result. Google's guidance describes discovery over several weeks in a compliant setup, not a guaranteed date.
6. **Media version:** write a distinct approximately 900–1,200-word practical explanation with a public example and link to the canonical report and GitHub. Submit an unpublished article to HackerNoon first or Towards AI next, respecting their current submission and prior-publication rules. Hugging Face and DEV are additional community routes.

先准备完整研究报告及可公开复现材料，确认作者资料和许可后再提交一个合适的预印本平台；上线后核验 Scholar；媒体解读使用独立文章，链接研究报告和代码。这里的页数和样本量是本项目的规划，不是保证录用或收录的门槛。

**Current status:** route research and planning are complete. Submission and indexing verification follow manuscript preparation. New publication spending: $0.

**当前状态：** 已完成渠道核实与规划。研究稿准备后，再进行投稿及收录核验。新增发表费用：0 美元。

## Recommended practical-publication routes / 技术短文优先方向

**For the media branch: HackerNoon first, Towards AI second.** Both provide editorial review for technology/practitioner articles, which fits a concise account of a working open-source tool and measured observations. For direct publication to the model-using community, Hugging Face is a complementary route. This prioritizes readership and editorial selection rather than journal indexing.

**媒体路线首选 HackerNoon，其次 Towards AI。** 两者都接受实践类技术文章并有编辑审核，适合介绍可运行的开源工具、方法与真实观察。Hugging Face 可作为直接面向模型使用者的补充渠道；选择重点是读者与编辑认可，不以学术索引为目标。

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
