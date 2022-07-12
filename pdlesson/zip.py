import pandas as pd

df = pd.read_csv("pdlesson/13TOKYO.CSV", header=None, encoding="shift_jis")

print(len(df))
print(df.columns.values)

# 1600006
results = df[df[2] == 1600006]
print(results[[2, 6, 7, 8]])

# 四谷を検索
results = df[df[8].str.contains("四谷")]
print(results[[2, 6, 7, 8]])
