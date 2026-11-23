# RadTag – LLM Prompts and Annotation Guidelines

Prompts and annotation guidelines for the LLM-assisted, change-centred annotation of longitudinal radiology report trajectories on the RadTag annotation platform. The annotation scheme is disease-agnostic; examples in the guidelines are taken from hepatocellular carcinoma (HCC) and bronchial carcinoma for illustration.

## Versions

| Version | Date | Purpose |
|---|---|---|
| **v1.0.0** | 25 September 2026 | Prompts and guidelines used for the LLM-generated annotations in the MIE 2027 submission (see below). Unchanged in this repository. |
| **v1.1.0** | 23 November 2026 | Revision based on the error analysis of the MIE 2027 evaluation and extension from report pairs to complete patient trajectories. Used for the pre-annotation of complete trajectories (HCC, bronchial carcinoma). |

Version v1.0.0 was used in:

> Sushko D, Sandmann S, Bickmann L, Behme D, Pech M, Varghese J. Annotating Disease Progression in Longitudinal Radiology Reports: An Integrated Platform Using Open-Weight LLMs. Manuscript submitted to Medical Informatics Europe (MIE) 2027, Tallinn, Estonia.

## Contents

| File | Description |
|---|---|
| `annotation_guidelines_v1.0.pdf` | Annotation scheme v1.0.0, as cited in the MIE 2027 submission |
| `prompts/prompts_v1.0.py` | System prompt and field-specific prompts v1.0.0, exactly as used for the MIE 2027 evaluation |
| `annotation_guidelines_v1.1.pdf` | Annotation scheme v1.1.0: annotation levels, attributes, controlled vocabulary, aggregation rules, examples |
| `prompts/prompts_v1.1.py` | System prompt and field-specific prompts v1.1.0 |
| `prompts/prompts_v1.0_to_v1.1.diff` | Line-by-line changes of the prompts from v1.0.0 to v1.1.0 |
| `CITATION.cff` | Citation metadata |
| `LICENSE` | License (CC BY 4.0) |

## Annotation levels

Each patient trajectory is annotated on three levels, each with its own prompt:

| Level | RadTag field | Input | Output |
|---|---|---|---|
| **Interval Note** | Vergleich | Preceding and current report, laboratory values | Comparability, overall interval label, change labels, essential change (free text) |
| **Finding-Specific Note** | Report (Befundbezogene Annotation) | Preceding and current report, laboratory values | Per finding: entity, location, finding status, direction of change, changed feature, delta/evidence |
| **Global Note** | Gesamt | Complete trajectory of reports and laboratory values | Overall status, context (free text) |

All output values are in German and use the controlled vocabulary defined in the guidelines. Laboratory values serve as supporting evidence only and never establish a radiological change by themselves.

The LLM receives only the free text of the reports (with dates) and, where available, laboratory values; no structured metadata such as index disease, modality or reference examination is passed. The inputs of v1.1.0 are identical to those of v1.0.0, except that the annotation prompts no longer use the laboratory values of the following time point.

## Changes in v1.1.0

| Change | Reason |
|---|---|
| Explicit definitions of comparability, aligned with the criteria of the MIE raters; comparability is decided first, and no trajectory is assigned to non-comparable report pairs | MIE: non-comparable pairs (e.g. NM whole-body vs. MR liver) rated as limited comparability and assigned a trajectory; comparability overestimated |
| PT+CT vs. CT only comparable if the CT component is diagnostic and acquired under comparable conditions | MIE: most bronchial carcinoma pairs were PT-CT/CT; comparability overestimated |
| “Nicht mehr nachweisbar” requires an explicit statement of absence and coverage of the region | MIE: a finding not mentioned in the follow-up report labelled as no longer detectable |
| Laboratory values strictly supporting; ignored for non-comparable pairs and across interventions; history and indication are context only | MIE: laboratory values used as primary evidence |
| “Unklar”/“Indeterminiert” refer to uncertainty about the change, not about the nature of a finding; rule for previously suspected findings | MIE: evident regression of a previously suspected finding labelled as indeterminate |
| The impression (Beurteilung) takes precedence over the description (Befund); new change label “Befundinterne Diskrepanz” | MIE limitation: contradictions between findings and impression |
| Orientation thresholds for relevant change (RECIST 1.1, mRECIST/LI-RADS Treatment Response, PERCIST 1.0), subordinate to the impression | MIE limitation: stable disease difficult to assert in bronchial carcinoma |
| Overall interval label and overall status refer to the index disease(s), determined from the reports; rules for several index diseases | Undefined in v1.0.0 |
| Interventional reports treated as events; explicit comparisons stated in the current report used when the preceding report is not comparable | Extension to complete trajectories with mixed modalities |
| New values: “Erstbeschreibung” (finding status), “Nicht beurteilbar” (direction of change), “Kein Vergleich möglich” and “Intervention” (change labels) | First examinations, events and non-comparable intervals |
| Finding complexes with examples for bronchial carcinoma; consistent definitions of the overall status (state at the end of the trajectory) | Mixed changes; contradictory definition of “Progredient” in v1.0.0 |
| Prediction (fallback) mode and laboratory values of the following time point removed from the annotation prompts and provided as a separate, optional prediction mode | Predictions mixed with annotations; future information in annotations used as training data |

## Optional prediction mode

Besides the annotation prompts, `prompts_v1.1.py` contains an optional prediction (follow-up) mode, comparable to the fallback mode of v1.0.0: `_DEFAULT_SYSTEM_FOLLOWUP`, `_DEFAULT_PROMPT_INTERVAL_FOLLOWUP` and `_DEFAULT_PROMPT_REPORT_FOLLOWUP`. It predicts the Interval Note or the Finding-Specific Note of the next examination from the last available report and the laboratory values, optionally including those of the following time point. The system prompt is identical to the annotation mode except for rule 1. The output uses the same fields, and the free text opens with “Vorhersage:”.

The prediction mode is not part of the annotation scheme v1.1.0 and has not been evaluated. Its outputs are predictions, not annotations; they must be stored and flagged as such and must not be used as training data.

## Model and settings

- **v1.0.0:** evaluated with the open-weight models `Gemma4:31b-it` and `Qwen3.8-27b`, run locally; no patient data left the institution.
- **v1.1.0:** intended for `Gemma4:31b-it`, run locally; evaluation pending.

## Prompt development

The annotation scheme, labels and aggregation rules were defined by the authors. The prompts v1.0.0 were drafted with the assistance of Claude Opus 5 (Anthropic); v1.1.0 was revised with the assistance of Claude Opus 5.5 (Anthropic) based on the error analysis of the MIE 2027 evaluation. All versions were reviewed, revised and tested by the authors and fixed before use. This repository contains no patient data; the screenshot in the guidelines uses synthetic data.

## Citation

v1.0.0:

> Sushko D. RadTag (v9_26): v1.0.0 – Prompts and annotation guidelines used for the MIE 2027 submission. Zenodo; 2026. doi:10.5281/zenodo.23468130

v1.1.0:

> Sushko D. RadTag: v1.1.0 – Prompts and annotation guidelines. Zenodo; 2026. doi:[to be added after the Zenodo release]

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

Dmitry Sushko, Institute of Medical Data Science / University Clinic for Radiology and Nuclear Medicine, University Medicine Magdeburg – dmitry.sushko@med.ovgu.de
