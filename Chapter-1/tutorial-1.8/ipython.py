import pandas as pd
interval_data = {
    "Temperature": [10, 15, 20, 25, 30],
    "GMAT_Score": [600, 650, 700, 750, 800],
    "SAT_Score (400 - 1600)": [1200, 1300, 1400, 1500, 1600],
    "Time": ["9:00", "10:00", "11:00", "12:00", "13:00"]
}
interval_df = pd.DataFrame(interval_data)
interval_df
%history -f ipython.py
