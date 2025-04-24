import pandas as pd
import pandas as pd
ordinal_data = {
    "Student Rank in a Class": ["1st", "2nd", "3rd", "4th", "5th"],
    "Educational Qualification": ["Graduate", "Undergraduate", "High School", "Graduate", "Undergraduate"],
    "Satisfaction Level": ["Good", "Average", "Bad", "Average", "Good"],
    "Income Level Range": ["80,000-100,000", "60,000-80,000", "40,000-60,000", "100,000-120,000", "50,000-70,000"],
    "Level of Agreement": ["Agree", "Neutral", "Disagree", "Neutral", "Agree"]
}
ordinal_df = pd.DataFrame(ordinal_data)
print(ordinal_df)
%history -f ipython.py
