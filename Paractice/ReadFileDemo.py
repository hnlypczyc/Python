#!/usr/bin/python
man= []
other = []
try:
    data = open(".\\Files\\test1.txt")
    for eachline in data:
        try:
            (role,words)=eachline.split(":",1)
            words = words.strip()
            if(role=='Man'):
                man.append(words)
            else:
                other.append(words)
        except ValueError:
            print("data value error")
    data.close

except IOError:
    print("file not exist")
print (man)
print (other)


try:
    manData = open(".\\Files\\man.txt",'a')
    otherData = open(".\\Files\\other.txt",'a')

    print(man,file=manData)
    print(other,file=otherData)
    manData.close()
    otherData.close()
except IOError:
    print("open file error")
