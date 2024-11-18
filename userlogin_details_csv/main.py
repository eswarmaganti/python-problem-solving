import pandas as pd
from pathlib import Path
from datetime import datetime

csv_file_path = Path().cwd() / "data.csv"

# reading the csv into a dataframe
df = pd.read_csv(csv_file_path)

# transforming the last_login column to a datetime object
df['last_login'] = pd.to_datetime(df['last_login'], format="%d-%m-%Y %H:%M:%S")

# calculating the days difference into a new column
df['days_diff'] = (datetime.now() - df['last_login']).dt.days

# filtering the user details which have logged in a year ago
result = df[df['days_diff'] >= 356]

print(result)