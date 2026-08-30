import pandas as pd
#python-fact-grounded-coding -> debugging
df = pd.read_csv("bay_area_modeling_table.csv", low_memory=False)
df1 = pd.read_csv("dashboard_data.csv", low_memory=False)
df2 = pd.read_csv("uc_admissions_summary_by_ethnicity.csv", low_memory=False)
df3 = pd.read_csv("uc_freshman_admission_by_discipline.csv", low_memory=False)
df4 = pd.read_csv("uc_transfer_admission_by_major.csv", low_memory=False)

data_frames = [df, df1, df2, df3, df4]
for data in data_frames:
    print(data)
    print()

