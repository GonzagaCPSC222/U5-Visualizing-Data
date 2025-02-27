import pandas as pd

df = pd.read_csv("bball.csv", index_col=0)
new_row_df = pd.DataFrame([["F",3,10,0]], columns=df.columns, index=["Noah Haaland"])
new_row_df.index.name = df.index.name
df = pd.concat([df, new_row_df])
df["CLASS"] = ["Sr", "So", "So", "So", "Sr", "Fr", "Fr", "Jr", "Jr", "Gr", "Sr", "Sr", "Sr", "Jr"]
print(df)