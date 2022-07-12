import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("pdlesson/test.csv", index_col=0)

# 国語の棒グラフ
df["国語"].plot.barh()
plt.legend(loc="lower left")
plt.show()

# 国語と数学の棒グラフ
df[["国語", "数学"]].plot.barh()
plt.legend(loc="lower left")
plt.show()

# c子の棒グラフ
df.loc["C子"].plot.barh()
plt.legend(loc="lower left")
plt.show()

# C子の円グラフ
df.loc["C子"].plot.pie(labeldistance=0.6)
plt.legend(loc="lower left")
plt.show()

# 行と列を入れ替えて実行(画像ファイルとして保存)
df.T.plot.bar()
plt.legend(loc="lower right")
# ply.show()
plt.savefig("pdlesson/bargraph.png")
