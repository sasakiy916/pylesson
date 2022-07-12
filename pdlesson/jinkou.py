import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("pdlesson/FEH_00200524_220712104723.csv",
                 index_col="全国・都道府県", encoding="shift_jis")
print(len(df))
print(df.columns.values)
df = df.drop("全国", axis=0)

# print(df["2021年"])
df["2021年"] = pd.to_numeric(df["2021年"].str.replace(",", ""))
df = df.sort_values("2021年", ascending=False)

df["2021年"].plot.bar(figsize=(10, 6))
plt.show()
