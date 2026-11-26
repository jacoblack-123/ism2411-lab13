# Jacob Lackey
# ISM2411 Lab 13 — First DataFrame — Retail Sales Explorer
#
# Self-Assessment
#
# 1. A boolean filter allows you to select rows that meet
# a specific condition. For example, you can filter sales
# to only show orders from the South region.
#
# 2. df["revenue"] selects one column as a Series, while
# df[["revenue"]] selects one column as a DataFrame.
# The difference matters when performing operations that
# require a DataFrame instead of a Series.
#
# 3. Pandas makes it easier to analyze large amounts of
# data quickly. Instead of manually sorting and filtering
# thousands of rows in Excel, pandas can do it with a few
# lines of Python code.
#
# Run command: python explore.py


import pandas as pd


# EXERCISE 1: Load it

df = pd.read_csv('data/retail_sales.csv')

print("EXERCISE 1: Load it")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


# EXERCISE 2: Filter by region

south = df[df['region'] == 'South']

print("\nEXERCISE 2: Filter by region")
print(len(south))
print(south.head())


# EXERCISE 3: Top 5 by revenue

print("\nEXERCISE 3: Top 5 by revenue")
print(df.sort_values('revenue', ascending=False).head(5))


# EXERCISE 4: Two-condition filter

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print("\nEXERCISE 4: Two-condition filter")
print(len(big_south))
print(big_south.head())


# EXERCISE 5: A new column

df['per_unit'] = df['revenue'] / df['quantity']

print("\nEXERCISE 5: A new column")
print(df.head())
print(df['per_unit'].mean())


# EXERCISE 6: Unique values

print("\nEXERCISE 6: Unique values")
print(df['region'].unique())
print(df['region'].value_counts())


# EXERCISE 7: Select columns

selected = df[['region', 'product', 'revenue']]

print("\nEXERCISE 7: Select columns")
print(selected.shape)


# EXERCISE 8: Save

df.to_csv('data/explored.csv', index=False)

print("\nEXERCISE 8: Save")
print("File saved successfully to data/explored.csv")