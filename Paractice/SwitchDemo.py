#!/usr/bin/python
from __future__ import division
def add(x,y):
    return x+y

def divide(x,y):
    return x-y

def Multiple(x,y):
    return x*y

def Chu(x,y):
    return x/y

'''
def operator(x,o,y):
    if o=="+":
        print (add(x,y))
    elif o=="-":
        print (divide(x,y))
    elif o=="*":
        print (Multiple(x,y))
    elif o=="/":
        print (Chu(x,y))
    else:
        pass

operator(1,"+",3)
'''
operator={"+":add,"-":divide,'*':Multiple,"/":Chu}
def f(x,o,y):
    print (operator.get(o)(x,y))

f(1,'*',2)
x=10
y=20
operator2 ={"+":x+y,"-":x-y,'*':x*y,"/":y/x}
print(operator2.get('+'))
