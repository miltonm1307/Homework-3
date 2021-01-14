import os
import csv

totalvotes = 0
vcountK = 0
vcountC = 0 
vcountL = 0 
vcountO = 0 
winner = 0  

with open ('Resources/election_data.csv','r') as my_data:
    reader=csv.reader(my_data)
    header=next(reader)

# The total number of votes cast
    for row in reader:
        totalvotes += 1
        candidate = row[2]
        if candidate == f'Khan':
            vcountK += 1
        if candidate == f'Correy':
            vcountC += 1
        if candidate == f'Li':
            vcountL += 1
        else:
            vcountO += 1
    
# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

print(f'Total Votes: {totalvotes}')
print(f'Khan: {vcountK/totalvotes}% ({vcountK})')
print(f'Correy: {vcountC/totalvotes}% ({vcountC})')
print(f'Li: {vcountL/totalvotes}% ({vcountL})')
print(f'OTooley: {vcountO/totalvotes}% ({vcountO})')
if vcountK > vcountC: 
    print(f'Winner is Khan')
elif vcountC > vcountL:
    print(f'Winner is Correy')
elif vcountL > vcountO:
    print(f'Winner is Li')
else: 
    print(f'Winner is OTooley') 