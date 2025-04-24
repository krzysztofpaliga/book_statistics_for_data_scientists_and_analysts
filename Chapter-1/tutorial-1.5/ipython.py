import pandas as pd
nominal_data =  {
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Religion": ["Hindu", "Muslim", "Christian", "Buddhist", "Jewish"],
    "Ethnicity": ["Indian", "Pakistani", "American", "Chinese", "Israeli"],
    "Color": ["Red", "Green", "Blue", "Yellow", "White"],
    "Electronic Appliances Ownership": ["Samsung", "LG", "Apple", "Huawei", "Sony"],
    "Person Favorite Meal": ["Biryani", "Kebab", "Pizza", "Noodles", "Falafel"],
    "Pet Preference": ["Dog", "Cat", "Parrot", "Fish", "Hamster"]
}
nominal_df = pd.DataFrame(nominal_data)
print(nominal_df)
%history -f ipython.py
