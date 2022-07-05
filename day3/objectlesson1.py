#userinfo=input("名前と血液型をカンマで区切って入力>>")
userinfo="sasaki,a"
[name,blood]=userinfo.split(",")
blood=blood.upper().strip()
print("{}さんは{}型なので大吉です".format(name,blood))

result = "banana".replace("a","o")
print(result)

aCount = "banana".count("a")
print(aCount)

def add(x,y):
    return x+y
print(type(add))
newadd=add
print(newadd(4,5))
