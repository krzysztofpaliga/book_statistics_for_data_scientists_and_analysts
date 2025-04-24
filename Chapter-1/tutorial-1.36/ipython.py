import pandas as pd
import numpy as np
prize_csv_df = pd.read_csv('./prize.csv')
z_scores = np.abs((prize_csv_df['laureates__share'] - prize_csv_df['laureates__share'].mean()) / prize_csv_df['laureates__share'].std())
z_scored.describe()
z_scores.describe()
z_scores.head()
prize_csv_df.index[z_scores > 2]
%history -f ipython.py
