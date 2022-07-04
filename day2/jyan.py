import random
while True:
    user=int(input("手を入力[0:グー,1:チョキ,2:パー])>>"))
    pc=random.randint(0,2)
    hands=["グー","チョキ","パー"]
    print(f"あなたは{hands[user]},PCは{hands[pc]}")
    if user == pc:
        print("あいこ")
        continue
    elif (user+3-pc)%3==1:
        print("あなたの負け")
    else:
        print("あなたの勝ち")
    break
