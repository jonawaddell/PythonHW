import csv
import os

# Files to load (Remember to change these)
budgetData = os.path.join("budget_data_1.csv")
file_to_output = 'budgetdata.txt'


# Read the csv and convert it into a list of dictionaries
with open(budgetData, newline="") as data1:
    reader = csv.reader(data1, delimiter=",")

    # use of next to skip first title row in csv file
    next(reader) 
    # create empty variable list
    revenue = []
    date = []
    rev_change = []

    # for each row in the csv file
    for row in reader:
        #assign column 2 to revenue variable
        revenue.append(row[1])
        #assign column 1 to date variable
        date.append(row[0])

    #print total months and total sum of revenues 
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

with open(file_to_output, w, newline="") as CsvFile:
    csvwriter = csv.writer(CsvFile, delimiter=",")
    csvwriter.writerrows()