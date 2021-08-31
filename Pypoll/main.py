import os
import csv

pypoll = os.path.join('Resources', 'election_data.csv')
pypoll = r"F:\Nga's Folder\Bootcamp\Week 3 -Python Home work\Pypoll\Resources\election_data.csv"

with open(pypoll) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #skip header
    pypoll_header = next(csvreader)
    
    #Calculate the total votes
    rows = 0
    totalvotesDic = {}
    for row in csvreader:
        rows += 1

        if row[2] not in totalvotesDic.keys():
            totalvotesDic[row[2]] = 1
        else:
            totalvotesDic[row[2]] += 1

print("Election Results")
print("-----------------------")
print(f"Total Votes: {rows}")
print("-----------------------")

#Calculate percentage & total votes next candidate 
for candidates in totalvotesDic.keys():
    candidates_score = candidates, "{:.2%}".format(totalvotesDic[candidates] / rows), "(", totalvotesDic[candidates], ")"
    print(candidates, "{:.2%}".format(totalvotesDic[candidates] / rows), "(", totalvotesDic[candidates], ")")

#Winner
winner = max(totalvotesDic, key=totalvotesDic.get)

print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

