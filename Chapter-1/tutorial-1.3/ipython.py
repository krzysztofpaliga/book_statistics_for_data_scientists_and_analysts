import pandas as pd
quantitative_df = pd.DataFrame({
"price": [300000, 250000, 400000, 350000, 450000], 
    "distance": [10, 15, 20, 25, 30], 
    "height": [170, 180, 190, 160, 175], 
    "weight": [70, 80, 90, 60, 75], 
    "salary": [5000, 6000, 7000, 8000, 9000], 
    "temperature": [25, 30, 35, 40, 45], 
    })
print(quantitative_df)
%history -f ipython.py
