---
version: 1
slug: "templates-index-html"
primary_target: "templates/index.html"
related_targets: ["static/css/app.css","static/js/app.js"]
---

## Surface

Scope: the single-page email checker.

Visitor mode: Operate.

Audience: students and lecturers demonstrating or reviewing this email phishing classifier.

Task: paste an email subject and body, run the repository's trained model, and read its classification and probability. Success means the user can try the actual model and distinguish its result from descriptive URL measurements.

Proof and content: `model_phishing.pkl` supplies classifications and probabilities; the repository's URL extractor supplies measured URL traits. The interface includes one clearly labeled synthetic sample using an `.example` domain.

Constraints: Indonesian copy; use the checked-in classifier; process submissions in the local app; do not represent URL traits as an explanation for the model's label or claim real-world detection performance. Honor the user's visual guardrails: use expressive non-cliché typography and a purposeful 12-column asymmetric layout with one dominant interaction; avoid Inter, Roboto, Fraunces, system-default display faces, purple/violet/indigo gradients, glows, repeated soft shadows, generic three-card feature grids, placeholder emojis, decorative badges, and unnecessary hover motion.

## Direction contract

THESIS: A focused phishing email checker with the clarity and annotation discipline of a research paper's proof margins. It refuses the generic dashboard's equal-weight metric cards.

OWN-WORLD: Margin Proof, chosen by the user. Warm paper, deep pine shell, and rust annotations; expressive editorial display type with a workhorse sans for controls and mono only for measurements. Thin rules, open surfaces, generous reading space. The signature move is a narrow annotated gutter for URL measurements, separated from the classifier's verdict.

STORY: The visitor brings a suspicious email, pastes its subject and body, and asks the existing model to classify it. The result gives a label and phishing probability. URL measurements stay in a separate section and are explicitly described as observations, not reasons for the prediction.

FIRST VIEWPORT: A dark pine masthead carries the Saring wordmark and actual model-file status. Beneath it, an 8/4 asymmetric introduction explains the task and input/output. The work area uses a 12-column grid: a spacious 7-column subject/body editor and one 5-column results column, initially in an honest empty state. The main action sits below the editor; after submission, the right column leads with the classification, then probability, annotated URL observations, and extracted URLs. On narrow screens the editor comes first and the report follows.

FORM: Annotated academic journal proofs, ranked third among seven grounded visual systems. Seed reference: `seed:a2c8b2b3ca1c008a`.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
