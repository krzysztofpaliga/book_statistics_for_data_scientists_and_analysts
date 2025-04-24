import pandas as pd
ratio_data = {
    "Height": [170, 180, 190, 200, 210],
    "Weight": [60, 70, 80, 90, 100],
    "Age": [20, 25, 30, 35, 40],
    "Speed": [80, 90, 100, 110, 120],
    "Tax Amount": [1000, 1500, 2000, 2500, 3000]
}
ratio_df = pd.DataFrame(ratio_data)
ratio_df
%history -f ipython.py
