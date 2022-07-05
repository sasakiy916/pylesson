import pprint
num = 2
list = [[(num-i)+(num*j) for j in range(5)] for i in range(2)]
pprint.pprint(list)
