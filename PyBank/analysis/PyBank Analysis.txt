import os
import csv
pybank = os.path.join('Resources','budget_data.csv')
pybank = r"F:\Nga's Folder\Bootcamp\Week 3 -Python Home work\PyBank\Resources\budget_data.csv"
with open(pybank) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #skip header
    pybank_header = next(csvreader)
    #Calculate the total months
    totalmonths = len(list(csvreader)) 

with open(pybank) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #skip header
    pybank_header = next(csvreader)
    #Calculate net total "Profit/Losses"    
    profit = 0
    for row in csvreader:
        profit += float(row[1])

with open(pybank) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #skip header
    pybank_header = next(csvreader)
    #Calculate the average of the changes in "Profit/Losses" over the entire period
    change = 0
    previousprofit = 0
    averageprofit = 0
    changelist = []
    month = []
    first_row = next(csvreader)
    previousprofit = int(first_row[1])
    for row in csvreader:
        change = int ((row[1])) - previousprofit
        previousprofit = int (row[1])
        changelist = changelist + [change]
        month = [month] + [row[0]]
        averageprofit = (sum(changelist))/len(changelist)
    
with open(pybank) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #skip header
    pybank_header = next(csvreader)

    total_months = 0
    month_of_change = []
    change_list = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999]
    total_net = 0

   # Extract first row to avoid appending to net_change_list
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in csvreader:
       # Track the total
       total_months += 1
       total_net += int(row[1])
       # Track the net change
       change = int(row[1]) - prev_net
       prev_net = int(row[1])
       change_list += [change]
       month_of_change += [row[0]]
       # Calculate the greatest increase
       if change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = change
       # Calculate the greatest decrease
       if change < greatest_decrease[1]:
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = change

#Print 
print ("Financial Analysis")
print (".................................................")
print("Total Months:", totalmonths)
print(f"Total: {profit}")
print(f"Average Change: {averageprofit}")
print(f"Greatest Increase In Profit: {greatest_increase}")
print(f"Greatest Decrease In Profit: {greatest_decrease}")

