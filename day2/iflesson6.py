print("すべての質問yまたはnで答えてください")
okane_aruka=input("お金に余裕はありますか?>>")
if okane_aruka == "y":
    onaka_suiteruka=input("お腹がすごくあいてますか?>>")
    nomitai_kibunka=input("ビールを飲みたいですか？>>")
    if onaka_suiteruka == "y" and nomitai_kibunka == "y":
        print("焼肉はいかがですか")
    elif onaka_suiteruka == "y":
        print("カレーはいかがですか")
    elif nomitai_kibunka == "y":
        print("焼き鳥はいかがですか")
    else:
        print("パスタはいかがですか")
    yashoku_iruka=input("夜食は必要ですか?>>")
    if yashoku_iruka == "y":
        print("コンビニのチキンはいかがですか")
else:
    print("家で食べましょう")
