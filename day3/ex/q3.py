import pprint
n=10
list=[[0+(i*10)-(j*10) for j in range(n)] for i in range(n)]
pprint.pprint(list)
