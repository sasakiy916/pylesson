#print("hello) #SyntacsError(文法エラー)
#print("hello" #SyntacsError

#IndentationError(インデントがずれてる9行目)
#x=10
#if(x<10):
#    print("hoge")
#else:
#print("hoge")

#TypeError(型が合わない)
#x=10
#print("hello"+x)#←ここがstr+intで型が違う

#TypeError: hello() takes 0 positional(位置、場所) arguments(引数) but 1 was given
#def hello():
#    print("hello")
#hello("world")

#IndexError: list index out of range
#my_list=[10,20,30]
#my_list[3]

#KeyError: 'hoo'
#my_dict={"hoge":1,"foo":2}
#print(my_dict["hoo"])

#ValueError: invalid literal for int() with base 10: 'arrow'
#x="arrow"
#x=int(x)

#UnboundLocalError: local variable 'a' referenced before assignment
#def hoge():
#    print(a)
#    a=10
#hoge()

#ModuleNotFoundError: No module named 'masu'
#import masu

#AttributeError: module 'math' has no attribute 'power'
#import math
#math.power(10,2)
