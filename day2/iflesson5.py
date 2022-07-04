score = int(input("点数>>"))
if 0<=score<=100:
    if score >= 60:
        print("合格")
    else:
        print("不合格")
else:
    print("不正な値です")
