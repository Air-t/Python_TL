'''
Created on 20 lut 2018
@author: LenovoAP
'''

'''
0. return TL raport sorted and grouped as normal
1. to work properly needs sheet revision increment (both detail and erection)
2. paperSize variable needs to be updated if size value on output is "UNKNOWN"
    to verivy what kind of drawings are used on project use advance selection in upper field:

from Drawing import *
dSheets = []
eSheets = []

sheets = GetAllDetailSheets()
for s in sheets:
    if (Drawing(s).size not in dSheets):
        dSheets.append(Drawing(s).size)

erection = GetAllErectionSheets()
for e in erection:
    if (Drawing(e).size not in eSheets):
        eSheets.append(Drawing(e).size)

print ("Detail sheet sizes:")
for item in dSheets:
    print (item)

print ("Erection sheet sizes: ")
for item in eSheets:
    print (item)
    
'''

saved_sds2_version = '7.312'
saved_python_version = (2, 7, 2, 'final', 0)

import json
import datetime
import re
from Drawing import *
now = datetime.datetime.now()

#selection file path (localHost only)
path = "E:\\TL\\TL"

#paper size to be updated if needed
paperSize = {"2-0 * 1-6" : "24\" x 18\"",
             "3-0 * 2-0" : "36\" x 24\"",
             "4-0 * 3-0" : "48\" x 36\"",
             "1-2 * 8 1/2" : "14\" x 8.5\"",
             "8 1/2 * 1-2" : "8.5\" x 14\"",
             "1-5 * 11" : "17\" x 11\"",
             "2-11 * 2-0" : "36\" x 24\"",
             }

#imports selection from a json file from a given directory
def importSelectioin(path):
    #opens json file
    with open(path) as json_file:
        #opens Selection list
        json_data = json.load(json_file)
        data = json_data['selection']
        #creates selection list to be returned
        selectionList = []
        #extracts data of a given format
        for item in data:
            listItem = item["text"]
            selectionList.append(re.sub("//.*?//", '', listItem))
        return selectionList

selection = importSelectioin(path)

initialDetailItems= []
initialErectionItems = []
tempList = []

sheets = GetAllDetailSheets()
for s in sheets:
    if Drawing(s).drawing_name in selection:
        actualPaperSize = str(Drawing(s).size)
        if (actualPaperSize in paperSize.keys()):
            actualPaperSize = paperSize[actualPaperSize]
        else:
            actualPaperSize = "UNKNOWN"
        tempList = [str(Drawing(s).drawing_name), str(Drawing(s).revision), "Detail Sheet", actualPaperSize, 0]
        initialDetailItems.append(tempList)
    else:
        pass

# sorts Detail Items
initialDetailItems = sorted(initialDetailItems, key=lambda x: x[0])

erection = GetAllErectionSheets()
for e in erection:
    if Drawing(e).drawing_name in selection:
        actualPaperSize = str(Drawing(e).size)
        if (actualPaperSize in paperSize.keys()):
            actualPaperSize = paperSize[actualPaperSize]
        else:
            actualPaperSize = "UNKNOWN"
        tempList = [str(Drawing(e).drawing_name), str(Drawing(e).revision), "Erection Sheet", actualPaperSize, 0]
        initialErectionItems.append(tempList)
    else:
        pass    

# sorts Erection Items
initialErectionItems = sorted(initialErectionItems, key=lambda x: x[0])

# PRINTS TL content
def printRaportRow(count, firstItem, lastItem):
    tS = [20,6,15,15,4]
    if(count == 1):
        print (str(firstItem[0]) + str(" "*(tS[0] - len(firstItem[0]))) + "|" + str(firstItem[1]) + str(" "*(tS[1] - len(firstItem[1]))) + "|" + str(firstItem[2]) + str(" "*(tS[2] - len(firstItem[2]))) + "|" + str(firstItem[3]) + str(" "*(tS[3] - len(firstItem[3]))) + "|" + "1    ")
    elif(count == 2):
        print (str(firstItem[0]) + " and " + str(lastItem[0]) + str(" "*(tS[0] - len(str(firstItem[0]) + " and " + str(lastItem[0])))) + "|" + str(firstItem[1]) + str(" "*(tS[1] - len(firstItem[1]))) + "|" + str(firstItem[2]) + str(" "*(tS[2] - len(firstItem[2]))) + "|" + str(firstItem[3]) + str(" "*(tS[3] - len(firstItem[3]))) + "|" + str(count) + str(" "*(tS[4] - len(str(count)))))
    else:
        print (str(firstItem[0]) + " thru " + str(lastItem[0]) + str(" "*(tS[0] - len(str(firstItem[0]) + " thru " + str(lastItem[0])))) + "|" + str(firstItem[1]) + str(" "*(tS[1] - len(firstItem[1]))) + "|" + str(firstItem[2]) + str(" "*(tS[2] - len(firstItem[2]))) + "|" + str(firstItem[3]) + str(" "*(tS[3] - len(firstItem[3]))) + "|" + str(count) + str(" "*(tS[4] - len(str(count)))))

def printHeader():
    print ("-"*70)
    print "TL created on: \t", now.strftime("%m-%d-%Y %H:%M")
    print ("-"*70)
    print ("RANGE OF DWG'S      |REV   |ITEM TYPE      |SIZE           |QTY  ")
    print ("-"*70)

def printDetailRaport():
    # prints report - without last row
    firstItem = []
    #counts items to be printed in a single row
    count = 1
    for i in range(len(initialDetailItems)-1):
        currentItem = initialDetailItems[i]
        nextItem = initialDetailItems[i+1]
        if (count==1):
            firstItem = currentItem
        if (currentItem[1:5] == nextItem[1:5]):
            count += 1
        else:
            printRaportRow(count, firstItem, currentItem)
            count = 1
    # prints last row of TL report
    firstItem = initialDetailItems[-(count)]
    lastItem = initialDetailItems[-1]
    printRaportRow(count, firstItem, lastItem)
    
def printErectionRaport():
    # prints report - without last row
    firstItem = []
    #counts items to be printed in a single row
    count = 1
    for i in range(len(initialErectionItems)-1):
        currentItem = initialErectionItems[i]
        nextItem = initialErectionItems[i+1]
        if (count==1):
            firstItem = currentItem
        if (currentItem[1:5] == nextItem[1:5]):
            count += 1
        else:
            printRaportRow(count, firstItem, currentItem)
            count = 1
    # prints last row of TL report
    firstItem = initialErectionItems[-(count)]
    lastItem = initialErectionItems[-1]
    printRaportRow(count, firstItem, lastItem)

def printSummary():
    print ("-"*70)    
    print ("Total items count: " + str(len(initialDetailItems)+len(initialErectionItems)))  
    print ("-"*70)
       
def addIndex(listOfLists):
    index = 0
    for i in range(len(listOfLists)-1):
        #numeric part of items
        currentItemNo = getNumericValue(listOfLists[i][0])
        nextItemNo = getNumericValue(listOfLists[i+1][0])
        #alphabetic part of items
        currentItemAl = getAlphaValue(listOfLists[i][0])
        nextItemAL = getAlphaValue(listOfLists[i+1][0])
        #determines if numeric value of the Item[i][0] and Item[i+1][0] are consecutive
        if ((nextItemNo - currentItemNo == 1) and (currentItemAl == nextItemAL)):
            listOfLists[i][4] = index
        else:
            listOfLists[i][4] = index
            index += 1
    #adds verification index to last item       
    if (len(listOfLists)):
        listOfLists[-1][4] = index
    else:
        pass
    return listOfLists
    
#returns numeric value of the string
def getNumericValue(string):
    numeric = ''
    for char in string:
        if (char.isdigit()):
            numeric += char
        else:
            pass
    return int(numeric)

#returns alphabetical part of the string - to provide comparison of alphapart
def getAlphaValue(string):
    alpha = ''
    for char in string:
        if (char.isalpha()):
            alpha += char
        else:
            pass
    return alpha

#TO BE IMPLEMENTED
#checks if duplicating items are in scope (like A1001 and 1001 or G1001 - number part duplicated)
def duplicateCheck():
    for i in range(len(initialDetailItems)-1):
        comparedItem = getNumericValue(initialDetailItems[i+1][0])
        for item in initialDetailItems:
            currentItem = getNumericValue(item[0])
            if (currentItem != comparedItem):
                pass
            else:
                print ("Items overlaps:", currentItem, comparedItem)

#adds verification index to items which potentially might be printed in single row
addIndex(initialDetailItems)
addIndex(initialErectionItems)

#prints whole TL report
printHeader()
if (len(initialErectionItems) > 0):
    printErectionRaport()
else:
    print ("No erection sheet items in selection.")
if (len(initialDetailItems) > 0):
    printDetailRaport()
else:
    print ("No detail sheet items in selection.")
printSummary()
#duplicateCheck()
