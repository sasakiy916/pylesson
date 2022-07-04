number = int(input("数値を入力>>"))
if number % 2 == 0:
    print("偶数")
else:
    print("奇数")

div = "偶数" if number %2 == 0 else "奇数"
print("{}です".format(div))

result="優" if number >=80 else "良" if number >=60 else "可" if number >=40 else "不可"
print(result)
