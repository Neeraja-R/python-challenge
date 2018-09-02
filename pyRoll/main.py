''' In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:



As an example, your analysis should look similar to the one below:

Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
In addition, your final script should both print the analysis to the terminal and export a text file with the results.  

Three columns: Voter ID, County, and Candidate.

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote.

____________________________________________________ 
'''

import os
import csv

pyRoll = os.path.join("..", "Resources", "election_data.csv")

voter_ID = []
count = []
candidate = []
listCandidates = []
percentVotes = []

with open(pyRoll, newline=" ") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader: 
        print(row)
    
    data = csvfile.split(",")
    while(row >= 1)
        voter_ID.append(float(data[0]))
        county.append(str(data[1]))
        candidate.append(str(data[2]))
    
        totalVotes = len(candidate)
        
        from collections import Counter 
            listCandidates_totalVotes = [Counter(candidate)]

            percentVotes = [(count(:float(i))/float(totalVotes))*100 for i in listCandidates]
            winner = max(percentVotes)   
                
            
            for s1, s2 in zip(listCandidates_totalVotes, percentVotes)
            
                
print("Election Results")
print("Total votes: " + totalVotes)
print (s1, s2)
print("Winner :" + winner)


    

