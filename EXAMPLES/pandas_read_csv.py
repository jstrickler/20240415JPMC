import pandas as pd

df = pd.read_csv('../DATA/sales_records.csv')  # Read CSV data into dataframe. Pandas automatically uses the first row as column names

print(df.head(5))  # Display first 5 rows of the dataframe (`df.describe(__n__)` displays n rows)
print()

print(df.describe())  # Get statistics on the numeric columns (use `df.describe(include='O')` for text columns)
print()

print(df.info())  # Get information on all the columns ('object' means text/string)
print()


df['total_sales'] = df['Units Sold'] * df['Unit Price']
df['smoosh'] = "wombat"
print(df)

print(df.info())
print(df.describe())

print('-' * 60)

print(df.head(10))
print('-' * 60)
print(df.describe(include="O"))



