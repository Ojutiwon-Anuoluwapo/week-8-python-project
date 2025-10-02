# Import pandas for data manipulation
import pandas as pd

# Load the metadata.csv file
df = pd.read_csv(r'C:\Users\User\Documents\python week 8 project\metadata.csv')

# Step 1: Identify missing values in each column
missing_counts = df.isnull().sum()
print("🔍 Missing values per column:\n", missing_counts)

# Step 2: Calculate the percentage of missing values per column
missing_ratio = df.isnull().mean()
print("\n📊 Missing value ratio:\n", missing_ratio)

# Step 3: Identify columns with more than 30% missing values
threshold = 0.3
high_missing = missing_ratio[missing_ratio > threshold]
print("\n⚠️ Columns with >30% missing values:\n", high_missing)

# Step 4: Drop columns with too many missing values
df_reduced = df.drop(columns=high_missing.index)

# Step 5: Fill remaining missing values with 'Unknown' for object columns
for col in df_reduced.select_dtypes(include='object').columns:
    df_reduced[col].fillna('Unknown', inplace=True)

# Step 6: Fill missing values in numeric columns with the column mean
for col in df_reduced.select_dtypes(include='number').columns:
    df_reduced[col].fillna(df_reduced[col].mean(), inplace=True)

# Step 7: Confirm that missing values have been handled
print("\n✅ Remaining missing values:\n", df_reduced.isnull().sum())

# Step 8: Preview the cleaned dataset
print("\n🧹 Cleaned Data Preview:\n", df_reduced.head(2))
# Step 9: Save the cleaned dataset to a new CSV file
df_reduced.to_csv('metadata_cleaned.csv', index=False)

# PREPARING DATA FOR ANALYSIS
                
# Import pandas for data manipulation
import pandas as pd

# Load the metadata.csv file into a DataFrame
df = pd.read_csv(r'C:\Users\User\Documents\python week 8 project\metadata.csv')

# 🗓️ Convert the 'publish_time' column to datetime format
# This allows for time-based filtering and analysis
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# 📆 Extract the year from the 'publish_time' column
# Useful for analyzing publication trends over time
df['publish_year'] = df['publish_time'].dt.year

# ✍️ Create a new column for abstract word count
# This helps quantify the length of each abstract
df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))

# 🧪 Preview the updated DataFrame with new columns
print(df[['publish_time', 'publish_year', 'abstract_word_count']].head(2))
