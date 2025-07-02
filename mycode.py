import pandas as pd
import os

#Creating a simple dataframe with column names

data = {'Name' : ['Alice', 'Bob', 'Charlie'],
         'Age' : [25, 30, 35],
        'City' : ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

#Adding a new row to the dataframe
new_row_loc = {'Name': 'David', 'Age': 28, 'City': 'San Francisco'}
df.loc[len(df.index)] = new_row_loc

data_dir = 'data'

os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")



