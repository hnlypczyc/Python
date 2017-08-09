#!/usr/bin/python

class Athele:

    def __init__(self,name,birth=None,score=[]):
        self.name = name
        self.birth = birth
        self.score = score

    def top3(self):
        return sorted(set([sanitize(item) for item in self.score]))[0:3]
    def add_score(self,new_score):
        self.score.append(new_score)
    def add_scores(self,new_score_list):
        self.score.extend(new_score_list)
    
def GetDataFromFile(filePath):
    try:
        with open(filePath) as Data:
                arrlist=Data.readline().strip().split(",")
                ath = Athele(arrlist.pop(0),arrlist.pop(0),arrlist)
                return ath
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
##sorted(set([sanitize(item) for item in arrlist]))[0:3]

print (james.name,"`s fastest times are:",james.top3())
james.add_score('1.01')
print(james.score)
print (james.name,"`s fastest times are:",james.top3())
james.add_scores(['0.02','0.9','2.45'])
print(james.score)
print (james.name,"`s fastest times are:",james.top3())


