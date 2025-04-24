import pandas as pd
people_df = pd.DataFrame({'name':['Alice', 'Bob', 'Charlie'], 'age':[25, 30, 35], 'gender':['F', 'M', 'M']})
people_df
new_df = people_df.drop('gender', axis='columns')
new_df
%history -f ipython.py
