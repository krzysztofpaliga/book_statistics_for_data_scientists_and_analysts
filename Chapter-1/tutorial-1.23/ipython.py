import pandas as pd
from IPython.display import display
diabities_df = pd.read_csv('./diabetes.csv')
print(diabities_df.columns)
display(diabities_df[['Glucose', 'Age']])
display(diabities_df[['Glucose', 'Age']].describe())
display(diabities_df[['Glucose', 'Age']].mode())
mode_range = diabities_df[['Glucose']].max() - diabities_df[['Glucose']].min()
print(mode_range)
diabities_df[['Glucose']].value_counts()
diabities_df.loc[:, ['Glucose', 'Age']]
diabities_df.iloc[0, 0:2]
diabities_df['Glucose'].corr(diabities_df['Age'])
diabities_df['Age'].corr(diabities_df['Glucose'])
diabities_df['Glucose'].corr(diabities_df['Age'], method='pearson')
diabities_df['Glucose'].corr(diabities_df['Age'], method='kendall')
diabities_df['Glucose'].corr(diabities_df['Age'], method='spearman')
%history -f ipython.py
