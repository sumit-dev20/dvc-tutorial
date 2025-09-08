import pandas as pd
import os

data = {
    "Name": ["Tony", "Steve", "Thor"],
    "Age": [45, 105, 1500],
    "City": ["NewYork", "Queens", "Asgard"],
}

df = pd.DataFrame(data)

new_raw = {"Name": "Pepper", "Age": 40, "City": "California"}

df.loc[len(df.index)] = new_raw

new_raw_2 = {"Name": "Natasha", "Age": 30, "City": "Moscow"}

df.loc[len(df.index)] = new_raw_2

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "students_data.csv")

df.to_csv(file_path)

print(f"dataframe saved to {file_path}")
