import pandas as pd
from IPython.display import display
diabities_df = pd.read_csv('./diabetes.csv')
print(diabities_df.columns)
diabities_df.head()
display(diabities_df[['Glucose']])
display(diabities_df['Glucose'])
display(diabities_df[['Glucose']].describe())
display(diabities_df[['Glucose']].mode())
mode_range = diabities_df[['Glucose']].max() - diabities_df[['Glucose']].min()
print(mode_range)
diabities_df[['Glucose']].value_counts()
%history -f ipython.py
