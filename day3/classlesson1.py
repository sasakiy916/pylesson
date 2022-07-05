class Hero:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def sleep(self,hours):
        print("{}は{}時間寝た".format(self.name,hours))
        self.hp += hours
        
print("start")
h=Hero("佐々木",100)
h.sleep(3)
print("{}のＨＰは現在{}です".format(h.name,h.hp))

scores1=[80,40,50]
scores2=[80,40,50]

print("scores1のidentity:{}".format(id(scores1)))
print("scores2のidentity:{}".format(id(scores2)))

if scores1 == scores2:
    print("同じ内容")
else:
    print("違う内容")

if id(scores1) == id(scores2):
    print("同じ存在")
else:
    print("違う存在")

names=list()
print("前:{}".format(id(names)))
names.append("松田")
print("後:{}".format(id(names)))


name="松田"
print("前:{}".format(id(name)))
name=name+"さん"
print("後:{}".format(id(name)))
