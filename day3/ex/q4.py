import pprint
list=[[2 if i-j>0 else 1 if i-j==0 else 0 for j in range(5)] for i in range(5)]
pprint.pprint(list)