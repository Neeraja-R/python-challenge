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
    while row >= [1]
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

import sys
sys.stdout=open("test.txt","w")
print("Election Results")
print("Total votes: " + totalVotes)
print (s1, s2)
print("Winner :" + winner)
sys.stdout.close()

    

