"""
text = input("何を記録しますか?>>")
file = open("diary.txt","a")
file.write(text + "\n")
file.close()
"""
text=input("何を記録しますか>>")
with open("diary.txt","a",encoding="utf-8") as file:
    file.write(text+"\n")
