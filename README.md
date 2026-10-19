# RadTag - LLM Prompts and Annotation Guidelines

Prompts and annotation guidelines for the LLM-assisted, change-centred annotation of longitudinal radiology report trajectories on the RadTag annotation platform. The annotation scheme is disease-agnostic; examples in the guidelines are taken from hepatocellular carcinoma for illustration.

This repository contains the **prompt version (v1.0.0, 25 September 2026)** used for LLM-generated annotations in:

> Sushko D, Sandmann S, Bickmann L, Behme D, Pech M, Varghese J. Annotating Disease Progression in Multimodal Longitudinal Radiology Reports: An Integrated RadTag Platform Using Open-Source LLMs. Manuscript submitted to Medical Informatics Europe (MIE) 2027, Tallinn, Estonia.

## Contents

| File | Description |
|---|---|
| `annotation_guidelines_v1.0.pdf` | Annotation scheme: annotation levels, attributes, controlled vocabulary, aggregation rules, examples |
| `prompts/prompts_v1.0.py` | System prompt and field-specific prompts, exactly as used for pre-annotation |

## Annotation levels

Each patient trajectory is annotated on three levels, each with its own prompt:

| Level | RadTag field | Input | Output |
|---|---|---|---|
| **Interval Note** | Vergleich | Prior and current report, laboratory values | Comparability, overall interval label, change labels, essential change (free text) |
| **Finding-Specific Note** | Report (Befundbezogene Annotation) | Prior and current report, laboratory values | Per finding: entity, location, finding status, direction of change, changed feature, delta/evidence |
| **Global Note** | Gesamt | Complete trajectory of reports and laboratory values | Overall status, context (free text) |

All output values are in German and use the controlled vocabulary defined in the guidelines. Laboratory values serve as supporting evidence only and never establish a radiological change by themselves.

## Model and settings

The same prompts were used with the following open-source models:

- "Gemma4:31b-it"
- "Qwen3.8-27b"

## Prompt development

The annotation scheme, labels and aggregation rules were defined by the authors. The prompts were drafted with the assistance of Claude Opus 5 (Anthropic) and were reviewed, iteratively revised and tested by the authors. The version in this repository was fixed before pre-annotation of the study dataset. This repository contains no patient data; the screenshot in the guidelines uses synthetic data.

## Citation

s. annotation_guidelines_v1.0

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

Dmitry Sushko, Institute of Medical Data Science / University Clinic for Radiology and Nuclear Medicine, University Medicine Magdeburg - dmitry.sushko@med.ovgu.de
