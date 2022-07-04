player1={"読書","昼寝","映画鑑賞","散歩","料理"}
player2={"テニス","将棋","料理","読書","旅行"}
input("心の準備ができたらEnterキーを押してください")
common=player1&player2
total=player1|player2
compatibility_rate=len(common) / len(total) * 100
print(f"相性度は{compatibility_rate}パーセントでした")
