import pandas as pd
df = pd.read_csv("bay_area_modeling_table.csv", low_memory=False)
df_2025 = df[df["fall_term"] == 2025]
total_applications = df_2025[df_2025["campus"] != "Universitywide"]["applicants"].sum()
tua = df_2025[df_2025["campus"] == "Universitywide"]["applicants"].sum()
average = round(total_applications / tua, 2)
print(average)