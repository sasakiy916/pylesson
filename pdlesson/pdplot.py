import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("pdlesson/test.csv")

# グラフを使って表示
df.plot()
plt.show()

# index_col=0とすることでグラフ表示の際のindexを名前列を使うことができる
df = pd.read_csv("pdlesson/test.csv", index_col=0)
# 棒グラフ
df.plot.bar()
# 見出しを右下
plt.legend(loc="lower right")
plt.show()

# 棒グラフ(水平)
df.plot.barh()
plt.legend(loc="lower left")
plt.show()

# 積み上げ棒グラフ
df.plot.bar(stacked=True)
plt.legend(loc="lower right")
plt.show()

# 箱ひげグラフ
df.plot.box()
plt.show()

# 面グラフ
df.plot.area()
plt.legend(loc="lower right")
plt.show()
