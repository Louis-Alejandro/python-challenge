import os
import csv

budgetdata_csv = os.path.join('..', 'Python','Homework', 'Starter_Code', 'PyBank', 'Resources','budget_data.csv')

def print_budgetprofitloss(date_profitloss):
    Date = int(date_profitloss[0])
    Profitlosses = int(date_profitloss[1])

    total_dates = Date+0


    

with open(budgetdata_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    date_to_check = input("find a date ")
    for row in csvreader:
        if date_to_check == row[0]:
            print_budgetprofitloss(row)

