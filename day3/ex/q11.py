import pprint
list = [["'_'" if i % 2 == 1 or
         (j % 2 == 0) else "'*'" for j in range(10)] for i in range(10)]
pprint.pprint(list)
