import pandas as pd
import os

data = {
    "Name": ["Tony", "Steve", "Thor"],
    "Age": [45, 105, 1500],
    "City": ["NewYork", "Queens", "Asgard"],
}

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "students_data.csv")

df.to_csv(file_path)

print(f"dataframe saved to {file_path}")
