import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df1 = pd.read_csv("pdlesson/csv/Preview_20220712113322.csv",
                  header=1, index_col="時点")
df2 = pd.read_csv("pdlesson/csv/Preview_20220712113538.csv",
                  header=1, index_col="時点")
df3 = pd.read_csv("pdlesson/csv/Preview_20220712113615.csv",
                  header=1, index_col="時点")
print(df1)
print(df2)
print(df3)

df1["年平均気温【℃】"].plot(label="平均気温")
df2["最高気温（日最高気温の月平均の最高値）【℃】"].plot(label="最高気温")
df3["最低気温（日最低気温の月平均の最低値）【℃】"].plot(label="最低気温")
plt.legend(loc="lower right")
plt.ylim(-10, 40)
plt.show()
