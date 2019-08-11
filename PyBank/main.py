# Calculate total number of months in budget_data.csv
# Two columns: Date, Profit/Losses

# Import dependencies
import os
import csv

# Specify the path to access our data
csv_path = os.path.join("Resources", "budget_data.csv")

# Create lists for each category/column of the csv
dates = []
PandLs = []

# Open and read the csv file
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Read the header row
    csv_header = next(csv_reader)
    
    # Fill our lists with data
    for date, PandL in csv_reader:
        dates.append(date)
        PandLs.append(int(PandL))

# Calculations for our analysis
total_months = len(dates)
total = sum(PandLs)

# Create a list of changes of "Profit/Losses" from month to month
monthly_change = []
for i in range(len(PandLs)):
    monthly_change.append(PandLs[i]-PandLs[i-1])

# Change the first value so as not to impact our search for max increase/decrease
monthly_change[0] = 0

# Calculate avg of changes in "Profit/Losses" over entire period
# First calculation is invalid so we subtract 1 from total months
avg_change = sum(monthly_change) / (total_months-1)

# Calculate greatest increase in profits over entire period
max_increase = max(monthly_change)

# Calculate greatest decrease in lossess over entire period
max_decrease = min(monthly_change)

# Merge dates and monthly change so we can find out max increase/decrease occurred 
PandL_dict = dict(zip(dates, monthly_change))

# Use the value to find the date (key) that the max increase occurred
#max_inc_month = (list(PandL_dict.keys())[list(PandL_dict.values()).index(max_increase)])
max_inc_month = max(PandL_dict, key=PandL_dict.get)

# Use the value to find the date (key) that the max decrease occurred
#max_dec_month = (list(PandL_dict.keys())[list(PandL_dict.values()).index(max_decrease)])
max_dec_month = min(PandL_dict, key=PandL_dict.get)

def analysis():
    print("Financial Analysis\n")
    print("-"*28 + "\n")
    print(f"Total Months: {total_months}\n")
    print(f"Total: ${total}\n")
    print("Average Change: ${:.2f}\n".format(avg_change))
    print(f"Greatest Increase in Profits: {max_inc_month} ${max_increase}\n")
    print(f"Greatest Decrease in Profits: {max_dec_month} ${max_decrease}\n")

# Print analysis to terminal
analysis()

# Specify the file to write to
output_file = "budget_data.txt"

with open(output_file, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("-"*28 + "\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total}\n")
    outfile.write("Average Change: ${:.2f}\n".format(avg_change))
    outfile.write(f"Greatest Increase in Profits: {max_inc_month} ${max_increase}\n")
    outfile.write(f"Greatest Decrease in Profits: {max_dec_month} ${max_decrease}\n")


