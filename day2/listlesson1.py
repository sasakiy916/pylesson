members=["工藤","松田","浅木"]
print(str(members[0]))

members.append("菅原")
members.append("湊")
members.append("朝香")

print(members)

del members[2]
print(members)

scores=[89,90,95]

total=sum(scores)
print(f'合計{total}')

a=[10,20,30,40,50]
b=a[1:3]
print(b)
c=a[2:]
d=a[:3]
e=a[:]
print(c)
print(d)
print(a[-2])

f=a[-2:]
print(f)
g=a[::-1]
print(g)

scores={"network":60,"database":80,"security":50}
print(scores)
print(scores["database"])
scores["programming"]=65
scores["security"]=55
print(scores)
