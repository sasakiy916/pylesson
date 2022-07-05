import pprint
list = [[(i+1)+(i+1)*j for j in range(9)] for i in range(9)]
pprint.pprint(list)
