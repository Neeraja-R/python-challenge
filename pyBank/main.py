import os
import csv

pyBank = os.path.join("..", "Resources", "budget_data.csv")

title = []
months = []
profits = []
monYear = []
profitMar = []

with open(pyBank, newline=" ") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader: 
        print(row)

    data = csvfile.split(",")     #columns split into two and define
    while (row >= 1)
        monYear.append(float(data[0]))
        profitMar.append(float(data[1]))

        months = enumerate(monYear)
        profits = sum(profitMar)
        difference = [profits[i+1] - profits[i] for i in range len[profits-1]]
            avgDiff = sum(difference)/len(profits-1)
            '''this is how you can make a loop in list form'''

        maxValue = max(difference)
            indexInc = difference.index(maxValue)
            incValues = data.pop(indexInc)
        minValue = min(difference)
            indexDec = difference.index(minValue)
            decValues = data.pop(indexDec)
                                      
print ("Financial Analysis")
print ("Total Months: " + months)
print ("Total: $" + profits)
print ("Average Change: $" + avgDiff)
print ("Greatest Increase in Profits: $" + incValue)
print("Greatest Decrease in Profits: $" + decValues)


import sys
sys.stdout=open("test.txt","w")
print ("Financial Analysis")
print ("Total Months: " + months)
print ("Total: $" + profits)
print ("Average Change: $" + avgDiff)
print ("Greatest Increase in Profits: $" + incValue)
print("Greatest Decrease in Profits: $" + decValues)
sys.stdout.close()
        



    
