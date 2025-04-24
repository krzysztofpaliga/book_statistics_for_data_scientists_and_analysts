import pandas as pd
discrete_data = {
    "Students": [25, 30, 35, 40, 45],
    "Cost": [500, 600, 700, 800, 900],
    "Employees": [100, 150, 200, 250, 300],
    "Players": [50, 40, 30, 20, 10],
    "Week": [7, 7, 7, 7, 7]
}
discrete_df = pd.DataFrame(discrete_data)
print(discrete_df)
%history -f ipython.py
