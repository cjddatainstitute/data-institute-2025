#  Common Pandas DataFrame Operations

This cheat sheet covers the most frequently used operations in Pandas when working with DataFrames.

---

##  1. Inspecting and Exploring Data

| Task                      | Code Example                    |
|---------------------------|---------------------------------|
| View top rows             | `df.head()`                     |
| View structure (rows, cols) | `df.shape`, `df.info()`      |
| View summary stats        | `df.describe()`                 |
| List column names         | `df.columns`                    |
| Check missing values      | `df.isna().sum()`               |
| Preview unique values     | `df['column'].unique()`         |

---

##  2. Cleaning Data

| Task                              | Code Example                                |
|-----------------------------------|---------------------------------------------|
| Drop missing values               | `df.dropna()`                                |
| Fill missing values               | `df.fillna(0)` or `df['col'].fillna('N/A')`  |
| Remove duplicates                 | `df.drop_duplicates()`                       |
| Rename columns                    | `df.rename(columns={'old': 'new'})`          |
| Convert types (e.g., str → float) | `df['col'] = df['col'].astype(float)`        |
| Strip strings                     | `df['col'] = df['col'].str.strip()`          |

---

##  3. Filtering and Subsetting

| Task                                  | Code Example                                    |
|---------------------------------------|-------------------------------------------------|
| Filter rows by condition              | `df[df['Price'] > 500000]`                      |
| Filter by multiple conditions         | `df[(df['Beds'] >= 3) & (df['City'] == 'Atlanta')]` |
| Select specific columns               | `df[['Address', 'Price']]`                      |
| Drop a column                         | `df.drop('column', axis=1)`                     |

---

##  4. Transforming Columns

| Task                                 | Code Example                                        |
|--------------------------------------|-----------------------------------------------------|
| Create new column                    | `df['Price_per_sqft'] = df['Price'] / df['SqFt']`  |
| Apply a function                     | `df['col'].apply(lambda x: x.upper())`             |
| Convert date column                  | `pd.to_datetime(df['Sold_Date'])`                  |
| Extract parts of date                | `df['Year'] = df['Sold_Date'].dt.year`             |

---

##  5. Aggregating and Grouping

| Task                                  | Code Example                                       |
|---------------------------------------|----------------------------------------------------|
| Group by column                       | `df.groupby('City').mean()`                        |
| Group and count                       | `df.groupby('City').size()`                        |
| Multiple aggregations                 | `df.groupby('ZIP')['Price'].agg(['mean', 'count'])`|

---

##  6. Sorting and Ranking

| Task                                  | Code Example                  |
|---------------------------------------|-------------------------------|
| Sort by column                        | `df.sort_values('Price')`     |
| Sort descending                       | `df.sort_values('Price', ascending=False)` |

---

##  7. Exporting and Saving

| Task               | Code Example                     |
|--------------------|----------------------------------|
| Export to CSV      | `df.to_csv('output.csv', index=False)` |
| Export to Excel    | `df.to_excel('output.xlsx')`     |
