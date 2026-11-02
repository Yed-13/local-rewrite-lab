# Evaluation record

Test date: November 2, 2026. Detector: GPTZero Premium, Advanced AI Scan, UI model 4.1o. Screenshots were taken from a logged-in Chrome session. Seven earlier reports were re-scanned to capture screenshots; the displayed results matched the earlier reports. Repeat captures are not additional independent samples.

## Initial optimized document

The first document scored AI 93%, Mixed 7%, Human 0%. Its source-reviewed rewrite scored AI 0%, Mixed 0%, Human 100%. The opening paragraphs used own-style prompting, and the later paragraphs used direct prompting. Manual corrections were included in the measured workflow. This was an optimized case, separate from the subsequent cross-document comparison.

## Three new complete documents

The three new documents were selected before checking their baseline scores. Both one-pass configurations were fixed, generated and source-reviewed before detector testing. No additional rewrite rounds were selected from these scores.

| Document | Original Human / Mixed / AI | Direct: Human / Mixed / AI | Own-style: Human / Mixed / AI |
|---|---|---|---|
| Incident response plan | 0 / 0 / 100 | 0 / 0 / 100 | 75 / 0 / 25 |
| Stakeholder and team analysis | 0 / 0 / 100 | 0 / 0 / 100 | 44 / 0 / 56 |
| Healthcare data ethics | 0 / 0 / 100 | 90 / 0 / 10 | 43 / 0 / 57 |

The 75% and 90% candidates were classified Human. The 44% and 43% candidates were Uncertain and would lean AI if forced to classify. The remaining two candidates were classified AI. Thus the fixed own-style configuration produced a Human classification in one of the three new documents. These document-level probabilities are not a general pass rate. All recorded AI Paraphrased subprobabilities were 0%.

The initial document is an optimized example; selecting the best of two candidates for each new document is also a selection step. Results for both candidates are retained in [results.csv](evidence/results.csv), alongside scan dates, model version, runtime and review-edit counts.

## Source review and material

Raw generations changed roles, conditions and some claim strengths. Examples included merging an owner and an office manager, replacing “may be stealing” with “is stealing,” changing a deadline, strengthening “helps” into “ensures,” and dropping a citation. Six cross-document candidates received 81 review edits, including substantive repairs and conservative wording restoration, before scanning. Tables, references and original end matter were preserved.

The evaluation documents and personal style reference remain private. They are not distributed for exact text-level reproduction. The bundled fictional AI-generated example is a deployment sample and did not produce the reported detector scores.

The tested style reference was the first 2,800 characters of a self-authored older text, approximately 467 English words. No minimum sample size, larger-corpus advantage, new fine-tuning or forum-corpus advantage was established in this experiment.

## Screenshot handling

Full detector-panel captures are retained privately. Public derivatives crop only surrounding interface content; the actual classification, all displayed probabilities and detector version remain intact. Full-capture records included “Text up-to-date” and word counts. Public [index.json](evidence/index.json) records capture times, scan times, words and probabilities. Images do not contain private document text or account identifiers.

## Resources

Thirty local generation calls for the three new documents took 383.99 seconds in total, excluding source review and document handling. Their nine detector comparisons covered 7,994 words. The inference model ran on an M3 Pro with 18GB unified memory. No external generation API or additional GPU was purchased for those comparisons. GPTZero scans used an existing paid membership.


## Cross-detector extension

The same reviewed texts were tested on ZeroGPT, Sapling, QuillBot and Pangram. The additional indicators did not reproduce the large GPTZero improvements. Scope, native metrics and all paired results are reported in [cross-detector replication](CROSS_DETECTOR.md).

## Expanded services / 扩展平台

See [the expanded detector comparison](EXPANDED_EVALUATION.md) for 31 additional completed scans, full-document and paragraph-level results, and the newly measured services.
