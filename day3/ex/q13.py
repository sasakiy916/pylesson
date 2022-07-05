import pprint
list = [[(10-i)-j for j in range(10-i)] for i in range(10)]
pprint.pprint(list)
