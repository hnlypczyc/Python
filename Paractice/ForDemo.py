#!/usr/bin/python
for x in "abcde":
    print ("hello "+ x)
    num = 0
for i in range(1,101):
    num = num + i
print (num)

d = {1:'0001',2:'0002',3:'0003'}
for k in d:
    print(k)
    print(d[k])
print (d.items())

for k,v in d.items():
    print(k)
    print(v)
