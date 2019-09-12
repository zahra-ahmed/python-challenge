import os
import csv

# file path
budget_csv = os.path.join('budget_data.csv')

# create lists to put csv data into
month_list = []
pl_list = []
change_list = []


# Read in the CSV file
with open(budget_csv, newline='') as csvfile:

    # Split the data on commas and identify headers
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # take data from csv file and put into lists
    for row in csvreader:
        
        month_list.append(row[0])

        pl_list.append(int(row[1]))


# total number of months included in the dataset
total_months = len(month_list)

# net total amount of profit/loss
net_pl = sum(pl_list)

# average of the changes in profit/loss        
for x in range(len(pl_list)-1):
    change_list.append(int(pl_list[x+1])-int(pl_list[x]))
pl_average = round(sum(change_list) / len(change_list), 2)

# greatest increase in profit/loss
greatest_increase = int(change_list[0])
for y in range(len(change_list)):
    if int(change_list[y]) > int(greatest_increase):
        greatest_increase = int(change_list[y])
        highest_month = month_list[y+1]

# greatest decrease in profit/loss
greatest_decrease = int(change_list[0])
for y in range(len(change_list)):
    if int(change_list[y]) < int(greatest_decrease):
        greatest_decrease = int(change_list[y])
        lowest_month = month_list[y+1]
    
    
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_pl}")
print(f"Average Change: ${pl_average}")
print(f"Greatest Increase in Profits: {highest_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease})")


# write into txt file

#file path
text_file = os.path.join('financial_analysis.txt')

with open(text_file, 'w') as text:
    text.write(f"Financial Analysis\n")
    text.write(f"---------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${net_pl}\n")
    text.write(f"Average Change: ${pl_average}\n")
    text.write(f"Greatest Increase in Profits: {highest_month} (${greatest_increase})\n")
    text.write(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease})\n")





    



