import pandas as pd
json_df = pd.read_json('./prize.json')
json_df
data = json_df['prizes']
prize_df = pd.json_normalize(data)
prize_df
prize_df.info()
prize_df.head()
import requests
response = requests.get("https://api.nobelprize.org/v1/prize.json")
data = response.json()
data
prize_json_df = pd.json_normalize(data, record_path='prizes')
prize_json_df
prize_csv_df = pd.read_csv('./prize.csv')
prize_csv_df
import numpy as np
arr = np.loadtxt('./diabetes.csv', delimeter=',', skiprows=1)
arr = np.loadtxt('./diabetes.csv', delimiter=',', skiprows=1)
print(arr)
arr = np.genfromtxt('./diabetes.csv', delimiter=',', names=True, missing_values='?', dtype=None)
arr.info()
print(arr)
%history -f ipython.py
