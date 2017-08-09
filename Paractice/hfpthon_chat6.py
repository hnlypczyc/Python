#!/usr/bin/python

james = []
julie = []
mikey = []
sarah = []



def GetDataFromFile(filePath):
    try:
        with open(filePath) as Data:
                arrlist=Data.readline().strip().split(",")
                Dict = {}
                Dict['name']=arrlist.pop(0)
                Dict['birth'] = arrlist.pop(0)
                arrlist = sorted(set([sanitize(item) for item in arrlist]))[0:3]
                Dict['score'] = arrlist
                return Dict
    except IOError as err:
        print ("File error: ",str(err))
        
def sanitize(time_string):

    if(time_string.find("-")>0 or time_string.find(":")>0):
        time_string = time_string.replace("-",".")
        time_string = time_string.replace(":",".")
    return time_string

james = GetDataFromFile('..\\Files\\hfpy_ch6_data\\james2.txt')
julie = GetDataFromFile("..\\Files\\hfpy_ch6_data\\julie2.txt")
mikey = GetDataFromFile("..\\Files\\hfpy_ch6_data\\mikey2.txt")
sarah = GetDataFromFile("..\\Files\\hfpy_ch6_data\\sarah2.txt")

##(name,birth)=(james.pop(0),james.pop(0))
##print(name,"`s fastest time are: ",sorted(set([sanitize(each_item) for each_item in james]))[0:3])
##jamesDict = {}
##jamesDict['name']=james.pop(0)
##jamesDict['birth'] = james.pop(0)
##jamesDict['score'] = james
print (james['name'],"`s fastest times are:",james['score'])

