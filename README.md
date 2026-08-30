# UC Data Challenge — Methodology & Workflow

This repository contains cleaned UC admissions data and scripts for exploratory analysis and modeling. The README documents the data sources, analysis rules, reproducible workflow, and best practices we used to produce robust, auditable results.

---

## At-a-glance
- Primary datasets (in repo root):
  - `bay_area_modeling_table.csv` — main modeling table
  - `dashboard_data.csv` — includes baseline model columns such as `expected_admit_rate` and `admit_rate_residual`
  - `uc_admissions_summary_by_ethnicity.csv` — authoritative race/ethnicity totals
  - `uc_freshman_admission_by_discipline.csv` — fall 2025 freshman discipline summary
  - `uc_transfer_admission_by_major.csv` — fall 2025 transfer major summary
- Main entrypoint: `main.py`
- Exploratory work: `experiment.py` (or new notebooks/scripts)
- Tools: pandas for tabular work, matplotlib/seaborn or Altair for visualizations

---

## Guiding data rules (critical)
These rules preserve dataset semantics and avoid misleading results:

1. Treat `Universitywide` as an independent row, not a sum of campus totals. Do not aggregate it with campus rows unless explicitly required.
2. Do not fill missing counts with zeros by default — blanks often indicate redactions or withheld values. Only replace with zero when the analysis explicitly calls for it, and document that choice.
3. When computing rates (admit, yield, etc.), always sum raw counts first then divide; do not average percentages across schools.
   - Correct: sum(admitted) / sum(applicants)
   - Incorrect: mean(admit_rate) across schools
4. Use `uc_admissions_summary_by_ethnicity.csv` as the authoritative source for race/ethnicity totals rather than summing school-level race columns.
5. Pay attention to year differences: policy and testing regimes changed for 2021+ (post SAT/ACT ruling). Treat pre- and post-policy years carefully when comparing trends.

---

## Methodology overview

1. Data ingestion
   - Load the cleaned CSVs from the repo root. These are the canonical inputs — do not overwrite them.
   - Keep provenance: if you generate derived files, save them under `output/` with clear filenames and a `README` in `output/` describing how they were produced.

2. Cleaning & validation (minimal and transparent)
   - Only perform minimal transformations required for the analysis (rename columns for clarity, convert types, parse dates).
   - Validate important assumptions with quick checks:
     - Unique campuses and `Universitywide` counts
     - No unintended duplicates by (year, campus, discipline, cohort)
     - Totals in `uc_admissions_summary_by_ethnicity.csv` match expected aggregates where applicable (but do not replace them)
   - Log or print rows with redacted/missing counts so the analyst can decide how to handle them.

3. Aggregation & rates
   - Group and sum raw counts before computing rates.
   - When stratifying by multiple dimensions (school × ethnicity), prefer hierarchical aggregation: compute totals at the needed level rather than averaging rates.
   - Use the ethnicity summary file for cross-checks and for race-level totals.

4. Analysis & modeling
   - Use `experiment.py` (or notebook) for exploratory plots and model prototyping.
   - Keep modeling baseline columns in `dashboard_data.csv` unmodified unless creating a new model version; add new model outputs as separate files or columns with version tags.
   - Document any model assumptions (features used, time windows, and handling of redacted values).

5. Visualization & communication
   - Produce concise plots and tables that answer specific questions; always state which file(s) and filters produced the result.
   - Annotate plots to note caveats (redacted counts, missing years, Universitywide treatment).

6. Reproducibility
   - Use a requirements file (e.g., `requirements.txt`) or environment spec.
   - Keep exploratory code separate from pipeline code: use `experiment.py` for exploration; use `main.py` or scripts under `scripts/` for reproducible tasks.
   - Save intermediate outputs with timestamps and source file references.

---

## Minimal code examples

Example: compute an admit rate by summing counts first (pandas):

```python
import pandas as pd

df = pd.read_csv("bay_area_modeling_table.csv")

# Group and sum raw counts
grouped = df.groupby(["year", "campus"], dropna=False).agg({
    "applicants": "sum",
    "admitted": "sum"
}).reset_index()

# Compute rate after summing
grouped["admit_rate"] = grouped["admitted"] / grouped["applicants"]
```

Example: cross-check ethnicity totals (use the authoritative file)

```python
eth_totals = pd.read_csv("uc_admissions_summary_by_ethnicity.csv")
# Use eth_totals instead of summing campus-level ethnicity columns for race totals
```

---

## Recommended workflow (short)
1. Start from the cleaned CSVs in the repo root.
2. Use pandas for filtering, grouping, and aggregation.
3. Keep experiments in `experiment.py` or a notebook. Do not overwrite the main dataset files.
4. Prefer minimal, readable transformations and add comments describing why each change was made.
5. Validate assumptions by printing or logging summary rows and differences against `uc_admissions_summary_by_ethnicity.csv`.

Common commands:
- Run the main script: `python main.py`
- Quick ad-hoc checks: `python -m pandas ...` or use small helper scripts.

---

## Output expectations & documentation
- Output formats: concise tables, clear plots, or short CSVs with versioned names.
- When reporting results, always:
  - Cite the input file(s) used (filename + path).
  - Describe the exact aggregation logic (e.g., "sum admitted and applicants across campuses, then divide").
  - Mention any data caveats that affect the conclusion (redaction, missing years, Universitywide inclusion).
- If a result hinges on how missing/redacted data were handled, include an alternate calculation demonstrating sensitivity.

---

## Use of AI tools
We used AI tools (for example, Le Chat Mistral and Gemini) strictly as debugging and brainstorming assistants to improve code correctness and efficiency. No code was copy-pasted from AI outputs; all final code and analysis decisions were authored and reviewed by the team.

---

## Repo structure (suggested)
- `bay_area_modeling_table.csv` (main input)
- `dashboard_data.csv`
- `uc_admissions_summary_by_ethnicity.csv`
- `uc_freshman_admission_by_discipline.csv`
- `uc_transfer_admission_by_major.csv`
- `main.py` — reproducible pipeline/entrypoint
- `experiment.py` — exploratory analysis and prototyping
- `scripts/` — small reusable scripts
- `output/` — derived outputs and artifacts (versioned)
- `requirements.txt` — environment dependencies

---

## Next steps and best practices
- Add `requirements.txt` if missing and a short CONTRIBUTING.md that documents how to run the pipeline.
- If you produce any derived datasets, save them to `output/` with a README entry describing how they were created.
- Consider adding unit tests for small, deterministic transformation functions (e.g., rate computations that check sum-before-divide behavior).

---

## Contact
If you want, I can:
- commit this README to the repository,
- generate a `requirements.txt` from the environment you used,
- or create a starter `experiment.ipynb` that demonstrates the "sum then divide" pattern and the ethnicity totals cross-check.
