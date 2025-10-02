#LOADING THE DATA

# Import the pandas library for data manipulation and analysis
import pandas as pd

# Load the CSV file into a DataFrame using the full file path
df = pd.read_csv(r'C:\Users\User\Documents\python week 8 project\metadata.csv')

# Display the first two rows of the DataFrame to preview the data
print(df.head(2))

# Show the data types of each column (e.g., int, float, object)
print(df.dtypes)

# Provide a concise summary of the DataFrame including column names, non-null counts, and data types
print(df.info())

# Generate basic statistical summaries for all numerical columns (mean, std, min, max, etc.)
print(df.describe())

# Count and display the number of missing (null) values in each column
print(df.isnull().sum())




#BASIC DATA EXPLORATION

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('metadata.csv')

# Check the dimensions of the DataFrame (rows, columns)
print("Dimensions:", df.shape)

# Display data types of each column
print("\nData Types:\n", df.dtypes)

# Check for missing values in each column
print("\nMissing Values:\n", df.isnull().sum())

# Generate basic statistics for numerical columns
print("\nSummary Statistics:\n", df.describe())
