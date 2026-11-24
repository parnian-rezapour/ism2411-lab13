# Self-Assessment
#
# 1. A Boolean filter checks each row against a condition and keeps only the rows
# where the condition is True.
#
# 2. df["revenue"] returns a Series, while df[["revenue"]] returns a one-column
# DataFrame. The difference matters when I want to keep the data in DataFrame
# form for later operations.
#
# 3. The biggest reason I would choose pandas is reproducibility. I can write the
# steps once and rerun the exact same process on the data instead of repeating
# manual Excel clicks each time.

import pandas as pd
df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2 - Filter by region

south = df[df["region"] == "South"]

print(len(south))
print(south.head())

# Exercise 3 - Top 5 by revenue

top_5 = df.sort_values("revenue", ascending=False).head(5)

print(top_5)

# Exercise 4 - Two-condition filter

big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print(len(big_south))
print(big_south.head())

# Exercise 5 - A new column

df["per_unit"] = df["revenue"] / df["quantity"]

print(df.head())
print(df["per_unit"].mean())

# Exercise 6 - Unique values

print(df["region"].unique())
print(df["region"].value_counts())

# Exercise 7 - Select columns

selected = df[["region", "product", "revenue"]]

print(selected.shape)

# Exercise 8 - Save

df.to_csv("data/explored.csv", index=False)
