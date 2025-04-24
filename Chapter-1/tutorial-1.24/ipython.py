import pandas as pd
from IPython.display import display
diabities_df = pd.read_csv('./diabetes.csv')
print(diabities_df.columns)
display(diabities_df[['Glucose', 'BMI', 'Age', 'Outcome']])
display(diabities_df[['Glucose', 'BMI', 'Age', 'Outcome']].describe())
diabities_df['Glucose'].corr(diabities_df['BMI'], method='pearson')
print(diabities_df.describe())
print(diabities_df.mode())
mode_range = diabities_df.max() - diabities_df.min()
print(mode_range)
diabities_df.corr()
diabities_df.corr().max()
diabities_df.corr()
%history -f ipython.py
