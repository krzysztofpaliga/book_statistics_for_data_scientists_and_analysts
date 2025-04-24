import random
population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_size = 3
sample = random.sample(population, sample_size)
sample
sample = random.sample(population, sample_size)
sample
sample = random.sample(population, sample_size)
sample
sample = random.sample(population, sample_size)
sample
sample = random.sample(population, sample_size)
sample
import pandas as pd
from IPython.display import display
diabities_df = pd.read_csv('./diabetes.csv')
sample_size = 5
num_rows = diabities_df.shape[0]
num_rows
random_indices = random.sample(range(num_rows), sample_size)
random_indices
sample_diabities_df = diabities_df.iloc[random_indices]
display(sample_diabities_df)
from sklearn.model_selection import train_test_split
population
test_size = 0.2
train_set, test_set = train_test_split(population, test_size=test_size, random_state=42)
train_set
test_set
%history -f ipython.py
