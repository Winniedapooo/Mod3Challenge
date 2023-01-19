import os
import csv

PyBank_csv = "PyBank/Resources/budget_data.csv"

with open (PyBank_csv, "r") as read:
    csv_read = csv.reader(read, delimiter=",")


print ("Financial Analysis")
print ('-------------------------------------')

# total number of months in the dataset




# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period