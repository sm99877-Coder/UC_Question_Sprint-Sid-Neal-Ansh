
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_colwidth", None)

df = pd.read_csv("uc_admissions_summary_by_ethnicity.csv", low_memory=False)
#df[(df.high_school=="MILPITAS HIGH SCHOOL")][
#    ['fall_term', 'campus', 'high_school', 'applicants', 'admits', 'admit_rate', 'enrollees', 'yield_rate', 'applicant_gpa']
#].sort_values(['fall_term', 'admit_rate'], ascending=False)

data = df[(df.entrant_level == "freshman") & (df.campus != 'Systemwide') & (df.fall_term == 2025) & ((df.count_type=='App')|(df.count_type=='Adm')) & ((df.ethnicity=='White')|(df.ethnicity =='Hispanic/Latino(a)'))][
    ['ethnicity', 'count_type', 'n']
]
ef = pd.read_csv("dashboard_data.csv", low_memory=False)
el = ef[(ef.fall_term == 2025)]
n_vals = list(data.n)
print(n_vals)
sorted(n_vals)
es = []
for value in n_vals:
  if value in el.index:
    e = el.loc[value]
    es.append(e)
print(es)
