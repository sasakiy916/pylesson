def hello():
    print("こんにちは")

hello()

def hello(name):
    print("こんにちは、{}さん".format(name))

hello("松田")

def profile(name,age,hobby):
    print("私の名前は{}です".format(name))
    print("年齢は{}歳です".format(age))
    print("趣味は{}です".format(hobby))

profile("佐々木",31,"ゲーム")

def plus(x,y):
    answer=x+y
    return answer

answer=plus(100,50)
print(answer) #150

def plus_and_minus(a,b):
    return a+b,a-b

next,prev=plus_and_minus(1978,1)

def eat(breakfast,lunch,dinner="カレー"):
    print("朝は{}を食べました".format(breakfast))
    print("昼は{}を食べました".format(lunch))
    print("夜は{}を食べました".format(dinner))
eat("トースト","おにぎり")
eat("バナナ","そば","焼肉")

def eat(breakfast,lunch="ラーメン",dinner="カレー"):
    print("朝は{}を食べました".format(breakfast))
    print("昼は{}を食べました".format(lunch))
    print("夜は{}を食べました".format(dinner))
eat(breakfast="納豆ご飯",dinner="カレーうどん")
eat(dinner="カレーうどん",breakfast="納豆ご飯")
eat("納豆ご飯",dinner="カレーうどん")

def eat(breakfast,lunch="ラーメン",dinner="カレー",desserts=()):
    print("朝は{}を食べました".format(breakfast))
    print("昼は{}を食べました".format(lunch))
    print("夜は{}を食べました".format(dinner))
    for d in desserts:
        print("おやつに{}を食べました".format(d))
eat("トースト","パスタ","カレー",("アイス","チョコ","ジャイアントコーン"))

def eat(breakfast,lunch="ラーメン",dinner="カレー",*desserts):
    print("朝は{}を食べました".format(breakfast))
    print("昼は{}を食べました".format(lunch))
    print("夜は{}を食べました".format(dinner))
    for d in desserts:
        print("おやつに{}を食べました".format(d))
eat("トースト","パスタ","カレー",("アイス","チョコ","ジャイアントコーン"))

def eat(**kwargs):
    for key in kwargs:
        print("{}に{}を食べました".format(key,kwargs[key]))
eat(朝食="納豆",遅めの朝食="パスタ",夕方のおやつ="カレーパン")
