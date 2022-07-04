import random
num = int(input("サイコロを何回ふる>>"))
dices=[random.randint(1,6) for _ in range(num)]
print(dices)
print("合計は",sum(dices),"でした")

num=int(input("サイコロを何回ふる>>"))
dices=[random.randint(1,6) for _ in range(num)]
print(dices)
print("出た目は",set(dices),"の",len(set(dices)))

num=int(input("100~1000の範囲の偶数をいくつ生成する?>>"))
data=[random.randrange(100,1000,2) for _ in range(num)]
data.sort(reverse=True)
print(num,"個生成しました！降順に表示します",data)
