## Import statements
from urllib import *
import urllib.request
from tkinter import *
from csv import *
import csv
from re import findall
import time

def StockMarket():
    
    coNameList = ['Apple', 'Microsoft', 'Google', 'Netflix', 'Cisco']
    coSymbolList = ['AAPL', 'MSFT', 'GOOG', 'NFLX', 'CSCO']
    coDict = {}
    myText = []
    myRow = []

    time1 = time.ctime()
    #write to CSV
    counter = 0
    if counter == 0:
        file = open("HW7Output.csv", 'w', newline='')
        csvWriter = csv.writer(file)
        csvWriter.writerow(['Time', 'Apple Stock Price', 'Apple Net Change', 'Apple Percent Change', 'Microsoft Stock Price', 'Microsoft Net Change', 'Microsoft Percent Change',
                            'Google Stock Price', 'Google Net Change', 'Google Percent Change','Netflix Stock Price', 'Netflix Net Change', 'Netflix Percent Change',
                            'Cisco Stock Price', 'Cisco Net Change', 'Cisco Percent Change'])
        file.close()
        counter = 1

    while int(time1[8:10]) < 12:
        time2 = time.ctime()
        myRow.append(time2)
        
        for i in range(len(coNameList)):
            myString = 'http://www.nasdaq.com/symbol/%s' % coSymbolList[i]
            #print(myString)
            response = urllib.request.urlopen(myString)
            html = response.read()
            text = html.decode()
            myText.append(text)
            tempName = coNameList[i]
            coDict[tempName] = coSymbolList[i]
    
        for y in range(len(coNameList)):
            StockRaw = findall('qwidget-dollar\"\>\$\d{1,5}[0-9]\.\d{0,3}[0-9]', myText[y])
            NetChangeRaw = findall('qwidget-cents (qwidget-Red\"\>\d{0,4}[0-9]\.\d{0,4}[0-9])|(qwidget-Green\"\>\d{0,4}[0-9]\.\d{0,3}[0-9])', myText[y])
            PercChangeRaw = findall('qwidget-percent (qwidget-Red\" style=\"white-space:nowrap\">\d{0,3}[0-9]\.\d{0,3}[0-9]%)|(qwidget-Green\" style=\"white-space:nowrap\">\d{0,3}[0-9]\.\d{0,3}[0-9]\%)', myText[y])
            #AppCommRatingRaw = findall('Consumer', myText[y])
            #print(AppStockRaw)
            #print(AppNetChangeRaw)
            #print(AppPercChangeRaw)

            if len(NetChangeRaw[0][1]) == 0:
                StockNum = findall('\d{0,4}[0-9]\.\d{0,3}[0-9]', StockRaw[0])
                NetChange = findall('\d{0,3}[0-9]\.\d{0,3}[0-9]', NetChangeRaw[0][0])
                PercChange = findall('d{0,3}[0-9]\.\d{0,3}[0-9]', PercChangeRaw[0][0])
            else:
                StockNum = findall('\d{0,4}[0-9]\.\d{0,3}[0-9]', StockRaw[0])
                NetChange = findall('\d{0,3}[0-9]\.\d{0,3}[0-9]', NetChangeRaw[0][1])
                PercChange = findall('d{0,3}[0-9]\.\d{0,3}[0-9]', PercChangeRaw[0][1])

            #print(StockNum)
            #print(NetChange)
            #print(PercChange)

            if len(NetChangeRaw[0][1]) == 0:
                NetChangeSign = findall('Red|Green', NetChangeRaw[0][0])
                PercChangeSign = findall('Red|Green', PercChangeRaw[0][0])
            else:
                NetChangeSign = findall('Red|Green', NetChangeRaw[0][1])
                PercChangeSign = findall('Red|Green', PercChangeRaw[0][1])

            #if len(AppNetChangeSign[0][1]) == 0:
                
            #print("app net sign:", NetChangeSign)
            #print("perc change:", PercChangeSign)
            netChangeSign = NetChangeSign[0]
            PercChangeSign = PercChangeSign[0]
            

            #print(NetChangeSign)
            #print(PercChangeSign)

            
            StockNum = StockNum[0]
            NetChange = NetChange[0]
            PercChange = PercChange[0]
            #print(StockNum)
            #print(NetChange)
            #print(PercChange)
            myRow.append(StockNum)
            myRow.append(NetChange)
            myRow.append(PercChange)
        print(myRow)
        time.sleep(1800)

        file = open("HW7Output.csv", 'a', newline='')
        csvWriter = csv.writer(file)
        csvWriter.writerow(myRow)
        file.close()
        myRow = []
        
        

#print("Start : %s" % time.ctime())
##time.sleep( 10 ) #use 1800seconds for data collection twice an hr
##print("End : %s" % time.ctime())



