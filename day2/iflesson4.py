gender=input("性別(男・女)>>")
age=int(input("年齢>>"))

if (gender == "男" and age>=18) or (gender=="女" and age>=16):
    print("結婚できます")
else:
    print("結婚できません")
