# AGENTS.md

This repository is a UC admissions data challenge. The goal is to analyze publicly available UC and California education data without breaking the assumptions documented in the dataset.

## Responsibilities

- Work with the CSV files in the repo root.
- Preserve the source data and avoid destructive edits to the raw files.
- Prefer small scripts and transformations that are easy to inspect.
- Keep analysis explainable and rooted in the README’s methodology notes.

## Critical rules

- `Universitywide` is not a campus total; it represents students admitted to at least one UC.
- Missing values are redacted and should not be treated as zeros without explicit justification.
- Aggregate by counts, not by average rate.
- Race/ethnicity totals should come from `uc_admissions_summary_by_ethnicity.csv`.
- Be mindful of changes in admissions policy across years.

## Suggested entry points

- `main.py` for the project’s main execution flow
- `experiment.py` for exploratory analysis and quick tests
- `README.md` for background and dataset semantics

## Keep in mind

The dataset is school-by-year-by-campus and is not individual-level student data. Every output should respect the aggregated and partially redacted character of the files.
