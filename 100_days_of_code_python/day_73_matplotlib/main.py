import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = './QueryResults.csv'
df = pd.read_csv(file_path)

# Basic data exploration
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())(df["m"])

