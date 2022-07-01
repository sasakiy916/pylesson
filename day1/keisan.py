a=10
b=5

answer=a+b
print(a,"+",b,"=",answer)

answer=a-b
print(a,"-",b,"=",answer)

answer=a*b
print(a,"*",b,"=",answer)

answer=a/b
print(a,"/",b,"=",answer)

answer=a//b
print(a,"//",b,"=",answer)

str = "Hello"*5
print(str)

x=10
x=x+10
print(x)

x=10
if x>0:
    print("正の整数です。")

if x>0:
    print("正の整数です。")
else:
    print("正の整数ではありません")

score=64
if score>80:
    print("優")
elif score>60:
    print("良")
elif score>40:
    print("可")
else:
    print("不可")

n=0
while n<10:
    print(n)
    n=n+1
print("終了")

for i in range(5):
    print(i)

for i in range(1,11):
    print(i,end="")

import random

num=random.randint(5,10)
print()
print("random:",num)

x=10
y=20
x,y=y,x
print(x,y)

x=10
print(type(x))

name="佐々木"
age=31
height=172.5
#print("私の名前は{}です。年齢は{}、身長は{}cm".format(name,age,height))
print(f"私の名前は{name}です。年齢は{age}、身長は{height}cm")
a="a";
x=10
y=type(a)(x)
print(type(y))
