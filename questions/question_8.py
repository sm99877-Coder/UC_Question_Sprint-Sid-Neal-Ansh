
import pandas as pd
df = pd.read_csv("uc_admissions_summary_by_ethnicity.csv", low_memory=False)
df_filtered = df[(df["entrant_level"] == "freshman") & (df["campus"] == "Systemwide") & (df["fall_term"] == 2025)]
df_pivot = df_filtered.pivot(
    index="ethnicity", columns="count_type", values="n"
).reset_index()
df_comparison = df_pivot[
    df_pivot["ethnicity"].isin(["White", "Hispanic/Latino(a)"])
].copy()
df_comparison["admission_rate"] = (
    df_comparison["Adm"] / df_comparison["App"]
) * 100
df_final = df_comparison[
    ["ethnicity", "App", "Adm", "admission_rate"]
].sort_values(by="admission_rate", ascending=False)
print(df_final.to_string(index=False))