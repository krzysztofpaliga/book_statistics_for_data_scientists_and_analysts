import pandas as pd
df = pd.DataFrame({
“age”: [25, 30, 35], # a quantitative column
    “gender”: [“female”, “male”, “male”], # a qualitative column
    “hair color”: [“black”, “brown”, “white”], # a qualitative column
    “marital status”: [“single”, “married”, “divorced”], # a qualitative column
    “salary”: [5000, 6000, 7000], # a quantitative column
    “height”: [6, 5.7, 5.5], # a quantitative column
    “weight”: [60, 57, 55] # a quantitative column
})
df = pd.DataFrame({
“age”: [25, 30, 35], # a quantitative column
    “gender”: [“female”, “male”, “male”], # a qualitative column
    “hair color”: [“black”, “brown”, “white”], # a qualitative column
    “marital status”: [“single”, “married”, “divorced”], # a qualitative column
    “salary”: [5000, 6000, 7000], # a quantitative column
    “height”: [6, 5.7, 5.5], # a quantitative column
    “weight”: [60, 57, 55] # a quantitative column
})
df = pd.DataFrame({
    “age”: [25, 30, 35], # a quantitative column
    “gender”: [“female”, “male”, “male”], # a qualitative column
    “hair color”: [“black”, “brown”, “white”], # a qualitative column
    “marital status”: [“single”, “married”, “divorced”], # a qualitative column
    “salary”: [5000, 6000, 7000], # a quantitative column
    “height”: [6, 5.7, 5.5], # a quantitative column
    “weight”: [60, 57, 55] # a quantitative column
})
df = pd.DataFrame({
    'age': [25, 30, 35], # a quantitative column
    'gender': ['female', 'male', 'male'], # a qualitative column
    'hair color': ['black', 'brown', 'white'], # a qualitative column
    'marital status': ['single', 'married', 'divorced'], # a qualitative column
    'salary': [5000, 6000, 7000], # a quantitative column
    'height': [6, 5.7, 5.5], # a quantitative column
    'weight': [60, 57, 55] # a quantitative column
})
print(df)
print(df.dtypes)
df.describe()
df.describe(include='O')
print(df['gender'].value_counts())
print(df['age'].value_counts())
import pandas.api.types as ptypes
print(f"Is string?: {ptypes.is_string_dtype(df['hair_color'])}")
print(f"Is string?: {ptypes.is_string_dtype(df['hair color'])}")
print(f"Is string?: {ptypes.is_string_dtype(df['salary'])}")
print(f"Is numeric?: {ptypes.is_numeric_dtype(df['weight'])}")
for col in df.columns:
    print(f"{col}:")
    print(f"Is numeric? {ptypes.is_numeric_dtype(df[col])}")
    print(f"Is string? {ptypes.is_string_dtype(df[col])}")
    print()
df.info()
df.head()
df.tail()
df.tail(1)
df.head(1)
from IPython.display import display
display(df.tail())
df.tail()
display(df.tail(1))
df.select_dtypes(include='number')
df.select_dtypes(include='object')
df.groupby('gender')
df
print(df.groupby('gender'))
display(df.groupby('gender'))
print(df.groupby('gender').describe())
print(df.groupby('gender').size())
print(df.groupby('gender').count())
print(df.groupby('gender').sum())
print(df.groupby(['gender', 'hair color']).sum())
df.columns
x = 42
y = 'Hello'
z = [1, 2, 3]
print(type(x))
print(type(y))
print(type(z))
%history -f ipython.py
