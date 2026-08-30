# UC Data Challenge Copilot Instructions

This repository contains UC admissions data for exploratory analysis and modeling. Keep changes focused on the data-analysis workflow and preserve the dataset semantics described in the README.

## Project context

- The main dataset is `bay_area_modeling_table.csv`.
- `dashboard_data.csv` includes model baseline columns such as `expected_admit_rate` and `admit_rate_residual`.
- `uc_admissions_summary_by_ethnicity.csv` is the authoritative file for race/ethnicity totals.
- `uc_freshman_admission_by_discipline.csv` and `uc_transfer_admission_by_major.csv` are fall 2025-only summaries.

## Data rules

- Treat `Universitywide` as a distinct row, not as a sum of campus totals.
- Do not fill missing counts with zeros unless the task explicitly requires it; blanks often represent redacted values.
- When computing rates, sum counts first and divide afterward. Avoid averaging percentages across schools.
- Use the ethnicity summary file for race totals instead of summing school-level race columns.
- Be careful with year differences: 2021+ used a different policy regime after the SAT/ACT ruling.

## Recommended workflow

1. Start from the cleaned CSVs in the repo root.
2. Use pandas for filtering, grouping, and aggregation.
3. Keep exploratory analysis in `experiment.py` or a new notebook/script; do not overwrite the main dataset.
4. Prefer minimal, readable transformations.
5. Validate assumptions against the README before claiming a conclusion.

## Common commands

- `python main.py`
- `python -m pandas ...` when running quick ad hoc checks

## Output expectations

- Prefer clear summaries, plots, or concise tables that answer a specific analysis question.
- Cite the relevant file and the logic used when explaining findings.
- If a result depends on a data caveat (redaction, missing years, or campus aggregation), explicitly mention it.
