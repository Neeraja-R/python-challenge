


In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
(Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset

The total net amount of "Profit/Losses" over the entire period

The average change in "Profit/Losses" between months over the entire period

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in losses (date and amount) over the entire period

As an example, your analysis should look similar to the one below:

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

__________________________________________-

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

        



    
