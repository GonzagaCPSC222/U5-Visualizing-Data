import pandas as pd

df = pd.read_csv("bball.csv", index_col=0)
print(df)

new_row_df = pd.DataFrame([["G",12,20,1]], columns=df.columns, index=["Joe Few"])
new_row_df.index.name = df.index.name
df = pd.concat([df, new_row_df])
print(df)

df["CLASS"] = ["Sr", "Jr", "Fr", "Fr", "Jr", "Fr", "So", "Fr", "Jr", "Sr", "Fr", "Sr", "Sr", "Fr"]
print(df)