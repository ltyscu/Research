#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jonathan
#
# Created:     20/09/2012
# Copyright:   (c) Jonathan 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import xlrd
d = 1
m = 1
y = 1
def setTime(dee,mmm,why):
    global d, m, y
    d = dee
    m = mmm
    y = why
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
        if(checkLeap(y)==True):
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
        return false
    elif(y%4==0):
        return true
    else:
        return false
    pass
def makeTwoChar(x):
    if(x<10):
        return "0"+str(x)
    else:
        return str(x)

def genFileName():
    global d,m,y
    return str(y)+str(makeTwoChar(m))+str(makeTwoChar(d))+"_rf_al.xls"
    pass
def test():
    workbook = xlrd.open_workbook(genFileName())
    worksheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name("Sheet1")
    #print(worksheet)
    #note to self life 5 calls headings
    for i in range(7,7+24):
        for j in range (1,10):
            print(worksheet.cell_value(i,j))
    #print(workbook)
    pass
def test2():
    setTime(1,1,2010)
    genFileName()
def main():
    test2()
    test()
    pass

if __name__ == '__main__':
    main()
