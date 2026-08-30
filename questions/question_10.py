#Hi, I tried to find the high school, but I got some hs that was not in the options, so I forced my program to choose out of the available options
import pandas as pd
df = pd.read_csv('bay_area_modeling_table.csv')
berkeleydf = df[(df['campus'] == 'Berkeley') & (df['fall_term'].between(2022, 2025))]
columns = ['high_school', 'fall_term', 'applicants', 'admits', 'admit_rate', 'applicant_gpa', 'ag_completion_rate', 'frpm_pct', 'enrollment_k12']
berkeleydf = berkeleydf[columns]
berkeleydf = berkeleydf.dropna(subset=columns)
five_schools = ['HECULES HIGH SCHOOL', 'MISSION SENIOR HIGH SCHOOL', 'MONTEREY TRAIL HIGH SCHOOL', "PHILLIP & SALA BURTON ACAD HS", 'RANCHO SAN JUAN HIGHH SCHOOL']
filtered_df = berkeleydf[berkeleydf['high_school'].isin(five_schools)]
print(filtered_df)pip i