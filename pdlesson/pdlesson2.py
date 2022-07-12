from tkinter import W
import pandas as pd
df = pd.read_csv("pdlesson/test.csv")
# 条件に合うデータを抽出
data_s = df[df["国語"] >= 90]
print(data_s)

# 複数条件(&(and),|(or),~(not)を使う)
data_s = df[(df["国語"] >= 90) & (df["数学"] >= 80)]
print(data_s)

# 集計
print("数学の最高点:", df["数学"].max())
print("数学の最低点:", df["数学"].min())
print("数学の平均点:", df["数学"].mean())
print("数学の中央値:", df["数学"].median())
print("数学の合計:", df["数学"].sum())

# データのソート
math_df = df.sort_values("数学")
print(math_df)
kokugo_df = df.sort_values("国語", ascending=False)
print(kokugo_df)

# 行と列の入れ替え
df_T = df.T
print(df_T)

# データをリスト化
li = df.values
print(li)

# csvに出力
kokugo_df.to_csv("pdlesson/export1.csv")
# インデックスを削除
kokugo_df.to_csv("pdlesson/export2.csv", index=False)
# インデックスとヘッダー削除
kokugo_df.to_csv("pdlesson/export3.csv", index=False, header=False)
