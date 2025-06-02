import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Save original shape and null counts
initial_shape = df.shape
initial_nulls = df.isnull().sum()

print(f"Initial Shape: {initial_shape}")
print("Initial Missing Values:\n", initial_nulls)

# Clean the dataset
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]  # Rename columns

# Fill missing values (future-proof way)
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Strip and title-case text fields
df['type'] = df['type'].str.strip().str.title()
df['title'] = df['title'].str.strip().str.title()
df['country'] = df['country'].str.strip().str.title()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned shape and nulls
cleaned_shape = df.shape
cleaned_nulls = df.isnull().sum()

print(f"\nCleaned Shape: {cleaned_shape}")
print("Remaining Missing Values (after cleaning):\n", cleaned_nulls)

# Save cleaned data
df.to_csv("cleaned_netflix_dataset.csv", index=False)

# Save summary report to text file
with open("cleaning_summary.txt", "w") as f:
    f.write(f"Initial Shape: {initial_shape}\n")
    f.write("Initial Missing Values:\n")
    f.write(initial_nulls.to_string())
    f.write(f"\n\nCleaned Shape: {cleaned_shape}\n")
    f.write("Remaining Missing Values:\n")
    f.write(cleaned_nulls.to_string())

print("\n Cleaning complete. Summary saved to 'cleaning_summary.txt' and cleaned CSV saved.")
