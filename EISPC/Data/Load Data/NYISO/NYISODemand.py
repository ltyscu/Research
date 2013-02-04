#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jonathan
#
# Created:     28/09/2012
# Copyright:   (c) Jonathan 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from numpy import *
import csv
import os.path
d = 1
m = 1
y = 1
def setTime(day,month,year):
    global d, m, y
    d = day
    m = month
    y = year
def iterateDay():
    global d, m, y
    d += 1
    if(d>monthLen(m,y)):
        d=1
        m += 1
        if(m>12):
            m =1
            y = y+1
    pass
def monthLen(m,y):
    if(m==1):
        return 31
    if(m==2):
        if(chkLeap(y)==True):
            return 29
        else:
            return 28
    if(m==3):
        return 31
    if(m==4):
        return 30
    if(m==5):
        return 31
    if(m==6):
        return 30
    if(m==7):
        return 31
    if(m==8):
        return 31
    if(m==9):
        return 30
    if(m==10):
        return 31
    if(m==11):
        return 30
    if(m==12):
        return 31
def chkLeap(y):
    if(y%400==0):
        return True
    elif(y%100==0):
        return False
    elif(y%4==0):
        return True
    else:
        return False
    pass
def makeTwoChar(x):
    if(x<10):
        return "0"+str(x)
    else:
        return str(x)
def gatherData(filename):
    print(filename)
    load = []
    sourceList = csv.reader(open(filename), dialect='excel')
    counter = -1
    hour = -1
    totload = 0
    lZone = "initial zone name"
    for row in sourceList:
#        print(row)
        if counter>=0:
#            print(counter)
#            print(counter %10)
            if(lZone != str(row[2])):
                totload = totload + float(row[4])
                counter += 1
            lZone = str(row[2])
#            print(row)
#            print(counter)
        if (counter%10==0) and (totload>0):
            hour += 1
#            print(hour)
#            print(totload)
            load.append(totload)
            totload = 0
            pass
        if(counter == -1):
            counter = 0
    return(load)
    pass
def timeData(filename):
    print(filename)
    load = []
    sourceList = csv.reader(open(filename), dialect='excel')
    counter = -1
    hour = -1
    totload = 0
    lZone = "initial zone name"
    for row in sourceList:
#        print(row)
        if counter>=0:
#            print(counter)
#            print(counter %10)
            if(lZone != str(row[2])):
                totload = str(row[0]) #totload + float(row[4])
                counter += 1
            lZone = str(row[2])
#            print(row)
#            print(counter)
        if (counter%10==0) and (totload>0):
            hour += 1
#            print(hour)
#            print(totload)
            load.append(totload)
            totload = 0
            pass
        if(counter == -1):
            counter = 0
    return(load)
    pass

def autoGenFileName():
    global d, m, y
    return genFileName(d,m,y)
def genFileName(day,month,year):
    return str(str(year)+makeTwoChar(month)+makeTwoChar(day)+"palIntegrated.csv")
def main():
    runTheYear()
    pass
def runTheYear():
    timeseries = []
    hourseries = []
    setTime(1,1,2004)
    for i in range(0,366):
        load = gatherData(autoGenFileName())
        time = timeData(autoGenFileName())
        count = 0
        for element in load:
            count += 1
            timeseries.append(element)
        for element in time:
            count += 1
            hourseries.append(element)
        if(count>24):
            print(autoGenFileName()+" : "+str(count))
        load = []
        iterateDay()
    savetxt("NYISOTS.csv", timeseries,delimiter=",", fmt="%f")
    savetxt("HNYISOTS.csv", hourseries,delimiter=",", fmt = "%s")
def test():
    #load = gatherData()
    #print(load)
    timeseries = []
    setTime(21,5,2004)
    load = gatherData(autoGenFileName())
    for element in load:
        timeseries.append(element)
    print(autoGenFileName())
    print(gatherData(autoGenFileName()))
    print(load)
    print(timeseries)
    print(len(timeseries))
#    for i in range(0,366):
#        print(autoGenFileName())
#        iterateDay()
if __name__ == '__main__':
    main()
    #test()
