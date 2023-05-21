import os
import csv

budgetdata_csv = os.path.join('..', 'Resources','budget_data.csv')
#Your task is to create a Python script that analyzes the records to calculate each of the following values:

months = []
net_total = []
pnl = []
greatestinp = 0
ginmon = str
greatestdep = 0
gdemon = str
# The total number of months included in the dataset
with open(budgetdata_csv, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        for row in csvreader:
            #add total months
            months.append(row[0])
            net_total.append(row[1])
        first = net_total[0]
        total_months = len(months)  
        g = 1   
        for x in net_total:
            if g < total_months: 
                next = net_total[g]  
                subs = (int(next) - int(first))
                pnl.append(subs)
                first = next
            g += 1
        nettotalresult = 0
       # x is the first value in the net_total,
       # and we are setting it equal to nettotal results 
       #and then pushing it back into the loop to continue the compliation of the entire row. 
        for x in net_total:
            nettotalresult += int(x)
        preaverage = 0
        for x in pnl:
            preaverage = preaverage + int(x)
        average = round(preaverage/len(pnl),2)
        pikachu = 1
        for x in pnl:
             if x > greatestinp:
                greatestinp = x
                ginmon = months[pikachu]
             elif x < greatestdep:
                greatestdep = x 
                gdemon = months[pikachu]    
             pikachu += 1

        

        
            
with open('Financial Analysis.txt', 'a') as pans:

    print('Financial Analysis', file=pans) 
    print('-------------------', file=pans)           
    print(total_months, file=pans)        
    print(nettotalresult, file=pans)
    print(average, file=pans)  
    print(ginmon, greatestinp, file=pans)      
    print(gdemon, greatestdep, file=pans)
         

 
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# #def print_budgetprofitloss(date_profitloss):
print(budgetdata_csv)

