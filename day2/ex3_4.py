month=int(input("今は何月ですか?(数字)>>"))
if month in [1,3,5,7,8,10,12]:
    print("31日まであります")
else:
    if month != 2:
        print("30日までです")
    else:
        print("1年で一番寒い月です")
    print("年が明けてから")
print("{}ヶ月が過ぎました".format(month))
