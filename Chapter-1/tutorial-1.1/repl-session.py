import pandas as pd
#
qualitative_data = {
#
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Michael'],
#
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Miami'],
#
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
#
    'Occupation': ['Engineer', 'Artist', 'Teacher', 'Doctor', 'Lawyer'],
#
    'Race': ['Black', 'White', 'Asian', 'Indian', 'Mongolian'],
#
    'Smartphone Brand': ['Apple', 'Samsung', 'Xiomi', 'Apple', 'Google']
#
}
#
#
qualitative_data
#
# {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Michael'], 'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Miami'], 'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 'Occupation': ['Engineer', 'Artist', 'Teacher', 'Doctor', 'Lawyer'], 'Race': ['Black', 'White', 'Asian', 'Indian', 'Mongolian'], 'Smartphone Brand': ['Apple', 'Samsung', 'Xiomi', 'Apple', 'Google']}
qualitative_df = pd.DataFrame(qualitative_data)
#
print(qualitative_df)
#
# Name           City  Gender Occupation       Race Smartphone Brand
# 0     John       New York    Male   Engineer      Black            Apple
# 1    Alice    Los Angeles  Female     Artist      White          Samsung
# 2      Bob        Chicago    Male    Teacher      Asian            Xiomi
# 3      Eve  San Francisco  Female     Doctor     Indian            Apple
# 4  Michael          Miami    Male     Lawyer  Mongolian           Google
print(qualitative_df.to_string(index=False))
#
# Name          City Gender Occupation      Race Smartphone Brand
#    John      New York   Male   Engineer     Black            Apple
#   Alice   Los Angeles Female     Artist     White          Samsung
#     Bob       Chicago   Male    Teacher     Asian            Xiomi
#     Eve San Francisco Female     Doctor    Indian            Apple
# Michael         Miami   Male     Lawyer Mongolian           Google
