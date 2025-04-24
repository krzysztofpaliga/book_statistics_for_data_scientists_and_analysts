import pandas as pd
diabities_df = pd.read_csv('./diabetes.csv')
diabities_df.isna()
diabities_df.isna().sum()
diabities_df.isnull().sum()
diabities_df.describe()
diabities_df.shape
diabities_df.size
diabities_df.memory_usage()
%history -f ipython.py
