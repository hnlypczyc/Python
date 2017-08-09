#!/usr/bin/python

james = []
julie = []
mikey = []
sarah = []

##try:
##    with open('..\\Files\\hfpy_ch5_data\\james.txt') as jamesData:
##        james = jamesData.readline().strip().split(",")
##
##    with open("..\\Files\\hfpy_ch5_data\\julie.txt") as julieData:
##        julie = julieData.readline().strip().split(",")
##    with open("..\\Files\\hfpy_ch5_data\\mikey.txt") as mikeyData:
##        mikey = mikeyData.readline().strip().split(",")
##
##    with open("..\\Files\\hfpy_ch5_data\\sarah.txt") as sarahData:
##        sarah = sarahData.readline().strip().split(",")
##except IOError as err:
##    print ("File error: ",str(err))

def GetDataFromFile(filePath):
    try:
        with open(filePath) as Data:
            return Data.readline().strip().split(",")
    except IOError as err:
        print ("File error: ",str(err))

james = GetDataFromFile('..\\Files\\hfpy_ch5_data\\james.txt')
julie = GetDataFromFile("..\\Files\\hfpy_ch5_data\\julie.txt")
mikey = GetDataFromFile("..\\Files\\hfpy_ch5_data\\mikey.txt")
sarah = GetDataFromFile("..\\Files\\hfpy_ch5_data\\sarah.txt")

##print(james)
##print(julie)
##print(mikey)
##print(sarah)

##print(sorted(james))
##print(sorted(julie))
##print(sorted(mikey))
##print(sorted(sarah))

def sanitize(time_string):

    if(time_string.find("-")>0 or time_string.find(":")>0):
        time_string = time_string.replace("-",".")
        time_string = time_string.replace(":",".")
    return time_string

##new_james = []
##new_julie = []
##new_mikey = []
##new_sarah = []
##for eachItem in james:
##    new_james.append(sanitize(eachItem))
##for eachItem in julie:
##    new_julie.append(sanitize(eachItem))
##for eachItem in mikey:
##    new_mikey.append(sanitize(eachItem))
##for eachItem in sarah:
##    new_sarah.append(sanitize(eachItem))
##
##def sanitize(time_string):
##
##    if(time_string.find("-")>0 or time_string.find(":")>0):
##        time_string = time_string.replace("-",".")
##        time_string = time_string.replace(":",".")
##    return time_string

##james = sorted([sanitize(each_item) for each_item in james])
##julie = sorted([sanitize(each_item) for each_item in julie])
##mikey = sorted([sanitize(each_item) for each_item in mikey])
##sarah = sorted([sanitize(each_item) for each_item in sarah])
##print(james)
##print(julie)
##print(mikey)
##print(sarah)
##
##for eachItem in james:
##    if eachItem not in new_james:
##        new_james.append(eachItem)
##for eachItem in julie:
##    if eachItem not in new_julie:
##        new_julie.append(eachItem)
##for eachItem in mikey:
##    if eachItem not in new_mikey:
##        new_mikey.append(eachItem)
##for eachItem in sarah:
##    if eachItem not in new_sarah:
##        new_sarah.append(eachItem)
##
##print(new_james[0:3])
##print(new_julie[0:3])
##print(new_mikey[0:3])
##print(new_sarah[0:3])

print(sorted(set([sanitize(each_item) for each_item in james]))[0:3])
