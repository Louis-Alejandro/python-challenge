import os
import csv
from collections import Counter
election_data_csv = os.path.join('..','Resources','election_data.csv')

id = []
county = []
candidate = []
ballotcount = 0
ccs = 0
dd = 0
rad = 0

with open(election_data_csv, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        for row in csvreader:
            id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
        ballotcount = len(id)
        countccs = candidate.count('Charles Casper Stockham')
        countdd = candidate.count('Diana DeGette')
        countrad = candidate.count("Raymon Anthony Doane")
        percentccs = round((countccs/ballotcount)*100,3)
        percentdd = round((countdd/ballotcount)*100,3)
        percentrad = round((countrad/ballotcount)*100,3)

with open('Election Results.txt', 'a') as bulbasaur:

    print("Election Results", file=bulbasaur)
    print("-------------------",file=bulbasaur)
    print(f"Total Votes: {ballotcount}",file=bulbasaur)
    print("-------------------",file=bulbasaur)
    print(f'Charles Casper Stockham: {percentccs}% ({countccs})',file=bulbasaur)
    print(f'Diane Degette: {percentdd}% ({countdd})',file=bulbasaur)
    print(f'Raymond Anthony Doane: {percentrad}% ({countrad})',file=bulbasaur)
    print("Election Results", file=bulbasaur)
    print('Winnder : Diana Degette',file=bulbasaur)
    print("-------------------",file=bulbasaur)
#for candidate in candidate_votes:
    #votes = candidate_votes[candidate]
            

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote
