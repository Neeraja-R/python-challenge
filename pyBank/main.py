


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


#read the csv file. 
#writing title for the output (see zipper example) 

import os
import csv

file = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data, 'r', newline=" ") as csvfile:
    csvreader = csv.reader(csvfile, delimiter " ") #csv reader specifiles delimiter and variable to hold contents
        print(csvreader) 
        data = list(csvreader)
        rowCount = len(data) #gets the number of rows ....use this later to write file 

    csvHeader = next(csvreader)
        print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

outPutPath = os.path.join("..", "pyRoll", "new.csv)  #this is simply added in here, must check 
    
    with open(outPutPath, 'w', newline = " ") as csvFileWrite:
    csvwriter = csv.writer(csvFileWrite, deliminiter = " ")

    csvwriter.writerow (["Financial Analysis"])
    csvwriter.writerow (["------------------"])
    csvwriter.writerow (["Total Months: " + str(rowCount)])




___________________________________________-

import os
import csv

pyBank = os.path.join("..", "Resources", "budget_data.csv")

title = []
months = []
profits = []

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
            avgDiff = [difference/len(profits-1]
            '''this is how you can make a loop in list form'''

        maxValue = max(difference)
            incGreat = difference.index(maxValue)
        
        minValue = min(difference)
            decGreat = difference.index(minValue)


        



    