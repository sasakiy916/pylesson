import random as rnd
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import pprint

df = pd.DataFrame(columns=["Aさん", "Bさん"])

for day in range(1, 32):
    weight_a = rnd.uniform(60, 63)
    weight_b = rnd.uniform(55, 58)
    df.loc[str(day)+"日"] = [weight_a, weight_b]
pprint.pprint(df)
df.plot(figsize=(8, 5))
plt.grid()
# plt.ylim(50, 65)
plt.show()
