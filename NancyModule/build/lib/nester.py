#!/usr/bin/python
import sys
def print_lol(the_list,indent=False,level=0,outPutType=sys.stdout):

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level,outPutType)

        else:
            if indent:
                print("\t"*level,end='',file=outPutType)
            print(each_item,file=outPutType)
            
