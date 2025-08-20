import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = './QueryResults.csv'
df = pd.read_csv(file_path)

# Basic data exploration
print("Dataset Shape:", df.shape) # (rows, columns)
print("\nData Types:\n", df.dtypes)
# print("\nColumns:", df.columns.tolist())
# print("\nFirst 5 rows:")
# print(df.head())
#
# # Check for missing values
# print("\nMissing values:")
# print(df.isnull().sum())
#
# print("\nLast five rows", df.tail())

print("\n Distinct m values", df['m'].unique())

print("\n Months count for each programmming language:",
df['TagName'].unique())

print(df.groupby('TagName').sum())


