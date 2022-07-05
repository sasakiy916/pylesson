import pprint
n=5
list = [[1 if j==0+i or j==n-i-1 else 0 for j in range(5)] for i in range(n)]
pprint.pprint(list)
