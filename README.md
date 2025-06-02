## Netflix Dataset Cleaning (Data Analyst Task)

This project demonstrates structured data cleaning and preprocessing using the Netflix Movies and TV Shows dataset from Kaggle. The objective was to transform raw data into a clean, analysis-ready format.

---

## Tools Used

- Python (Pandas)
- Python IDE / Command Line
- Git and GitHub for version control

---

## Repository Contents

| File Name                    | Description                                                |
|-----------------------------|-------------------------------------------------------------|
| cleaningdataset.py          | Python script for data loading, cleaning, and export        |
| netflix_titles.csv          | Raw dataset from Kaggle                                     |
| cleaned_netflix_dataset.csv | Cleaned and formatted dataset ready for analysis            |
| cleaning_summary.txt        | Summary of the changes made during the data cleaning process|
| README.md                   | Project documentation                                       |

---

## Cleaning Objectives

1. Handle missing data in key fields such as `director`, `cast`, `country`, `rating`, and `duration`.
2. Convert inconsistent formats to standardized ones (e.g., `date_added` to datetime).
3. Remove duplicate entries, if present.
4. Apply string normalization and formatting to ensure consistency across text fields.
5. Rename columns using `snake_case` for improved readability and usability.
6. Ensure correct data types across all columns.

---

## Summary of Cleaning Steps

| Step | Action                      | Description                                                        |
|------|-----------------------------|--------------------------------------------------------------------|
| 1    | Load dataset                | Loaded the dataset with shape (8807, 12)                           |
| 2    | Handle missing values       | Used `.fillna()` to replace nulls with domain-appropriate defaults |
| 3    | Format date fields          | Converted `date_added` to proper datetime format                   |
| 4    | Remove duplicates           | Checked and removed duplicates if any (none found)                 |
| 5    | Standardize column names    | Renamed columns to lowercase with underscores                      |
| 6    | Export cleaned dataset      | Saved the final dataset to `cleaned_netflix_dataset.csv`           |

---

## Code Walkthrough — `cleaningdataset.py`

import pandas as pd

**Load the raw dataset**

df = pd.read_csv("netflix_titles.csv")

print("Initial Shape:", df.shape)

**Display missing values**

print(df.isnull().sum())

**Fill missing values with meaningful defaults**

df['director'] = df['director'].fillna('Unknown')

df['cast'] = df['cast'].fillna('Not Available')

df['country'] = df['country'].fillna('Unknown')

df['rating'] = df['rating'].fillna('Not Rated')

df['duration'] = df['duration'].fillna('Unknown')

**Convert date_added to datetime**

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

**Remove duplicates**

df.drop_duplicates(inplace=True)

**Standardize column names to snake_case**

df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

**Display final shape**

print("Cleaned Shape:", df.shape)

**Save cleaned dataset**

df.to_csv("cleaned_netflix_dataset.csv", index=False)


**Note:** Warnings related to `inplace=True` and chained assignments were encountered due to newer pandas behavior. These can be avoided by using:

df['column'] = df['column'].fillna('value')

---

## Output Summary

Cleaned data sample:
![image](https://github.com/user-attachments/assets/a6faee80-1e75-4f93-8f38-b6a50d81189f)


All originally missing values were handled appropriately and the dataset is now suitable for exploratory data analysis or machine learning tasks.

---

## How to Run the Script

Ensure that `netflix_titles.csv` is present in the same directory, then run:

python cleaningdataset.py

The cleaned dataset will be saved as `cleaned_netflix_dataset.csv`.

---

## Applications

* Exploratory Data Analysis (EDA)
* Dashboard creation and visualization
* Data modeling and prediction
* Data wrangling practice for aspiring analysts

---

## Contact

For questions, collaborations, or feedback, please reach out through GitHub, Email or LinkedIn.

Email-10221shubham.s@gmail.com

Linkedin-www.linkedin.com/in/shubham-s-14ba6a283

---
