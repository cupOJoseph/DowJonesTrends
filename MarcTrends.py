import csv
import sys

#ifile  = open('HistorialPrices.csv', "rb")
ifile  = open('C:\\Users\\MLH-Admin\\Desktop\\HistoricalPrices.csv', "rb")
reader = csv.reader(ifile)

rownum = 0
segCounter = 0
difCounter = 0

differences = []#empty differences list
#Yearly = []# get the starting dates for each segment
differences.append([11])#make that shit 2d   ____
#####     #####                      ####  /    /
#   #     #   #             /\       #  #/    /
#   # # # #   #           /   \      #      /
#             #         /      \     #      #
#   # # # #   #       /_________\    #      #
#   #     #   #     /            \   #   \   \
#####     #####   /               \  #####\___\

year = 15

for row in reader:
    # Save header row
    if rownum == 0:
        header = row
    else: #all cases, not first row, this is all raw data
        if row[0].endswith(str(year)):
            #print "year is ", str(year)#year is unchanged
            if(difCounter <= 2):
                #get opening day 1, closing day 3
                if(difCounter == 0):
                    openingVal = row[1]
                    closingVal = row[4] #include this closing value incase the year changes and there arent 3 days in a row that we want to use
                    difCounter+= 1#increment to 1
                elif(difCounter == 2):
                    closingVal = row[4]
                    difCounter = 0
                    difVal = float(openingVal) - float(closingVal)
                    differences[15-year].append(difVal)
                else:#dif counter is 1, increment to 2
                    difCounter += 1 #increment dif counter to 2. built like this so its
                    closingVal = row[4]
                    #dynamic to change the number of days in a difference
        else:
            if(difCounter != 0):
                difVal = float(openingVal) - float(closingVal)
                differences[15-year].append(difVal)
            year -= 1#year has changed. start a new line
            difCounter = 1
            openingVal = row[1]
            #print "year is ", str(year)
        #create differences for every 3 days

    rownum += 1

ifile.close()
print 'differences:'
print differences
