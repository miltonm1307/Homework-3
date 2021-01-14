import os
import csv

#variables
month_count = 0
row_count = 0
total_sum = 0
rcount = 0
tsum = 0
last_month_value = 0
total_change = 0
monthly_change = 0
PreValue = 0
Diff = 0
DiffMax = 0 
DiffMin = 0


# The total number of months included in the dataset
with open ('Resources/budget_data.csv','r') as my_data:
    reader=csv.reader(my_data)
    header=next(reader)

    for row in reader:
        month = row[0]
        Amount = row[1]
        rowAmount = int(Amount)
        Diff =  rowAmount - PreValue
        month_count=month_count+1

    #print(f'Total Months : {month_count}')

  # The net total amount of "Profit/Losses" over the entire period
    #for row in reader: 
        row_count +=1
        total_sum += int(row[1])
    #print(f'Total: $ {total_sum}')

  # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    #for row in reader:
        if rcount != 0:
            total_change += int(row[1])-last_month_value
        rcount = rcount + 1
        last_month_value=int(row[1])
    #print(f'Average change in P/L: $ {total_change/rcount}')


    #for row in reader:

         #Placeholder to track greatest increase in profits (financial analysis)
        if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         #Placeholder to track greatest decrease in profits (financial analysis)
        if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month
    PreValue = rowAmount   

    print(f'Total Months : {month_count}')
    print(f'Total: $ {total_sum}')
    print(f'Average change in P/L: $ {total_change/rcount}')
    # Greatest increase in profit
    print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
    # Greatest decrease in profit
    print(f'Greatest Increase in Losses: {DiffMinDate} : ($ {DiffMin})')




