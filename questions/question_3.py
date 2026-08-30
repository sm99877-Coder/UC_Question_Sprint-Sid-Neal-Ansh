import pandas as pd
df = pd.read_csv("uc_freshman_admission_by_discipline.csv", low_memory=False)
df_overall = df[df["broad_discipline"] == "All disciplines"][
    ["campus", "admit_rate"]
].rename(columns={"admit_rate": "overall_admit_rate"})
df_cs = df[df["broad_discipline"] == "Computer Science"][
    ["campus", "admit_rate"]
].rename(columns={"admit_rate": "cs_admit_rate"})
df_comparison = pd.merge(df_renamed, ar_rename, on="campus")
df_comparison["cost"] = (
    df_comparison["overall_admit_rate"] - df_comparison["cs_admit_rate"])
df_comparison["cost_to_admission_ratio"] = (
    df_comparison["cost"] / df_comparison["cs_admit_rate"])
df_final = df_comparison.sort_values(
    by="cost_to_admission_ratio", ascending=False)
df_final["cost_to_admission_ratio"] = df_final[
    "cost_to_admission_ratio"
].round(2)
print(df_final)

