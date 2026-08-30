import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_colwidth", None)

df = pd.read_csv("bay_area_modeling_table.csv", low_memory=False)
df[(df.high_school=="MILPITAS HIGH SCHOOL")][
    ['fall_term', 'campus', 'high_school', 'applicants', 'admits', 'admit_rate', 'enrollees', 'yield_rate']
].sort_values(['fall_term', 'admit_rate'], ascending=False)
