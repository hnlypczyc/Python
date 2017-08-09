#!/usr/bin/python

try:

    data = open(".\\Files\\test1.txt")
    
    for each_line in data:
        try:
            l= each_line.split(":",1)
            '''
            print (l[0],end='')
            print(" Said",end='')
            print (l[1])
            '''
            (name,statement)=each_line.split(":")
            print(name,end='')
            print(" Said",end='')
            print(statement,end='')
            
        except:
            print ("data value error")
        
    data.close()
except:
    print ("File is not exist")
