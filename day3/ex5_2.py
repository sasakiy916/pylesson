def is_leapyear(year):
    return year%400==0 or (year%4==0 and year%100!=0)

year = int(input("何年>>"))
if is_leapyear(year):
    print(f"西暦{year}年は、うるう年です")
else:
    print(f"西暦{year}年は、うるう年ではありません")

