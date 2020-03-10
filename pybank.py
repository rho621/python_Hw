import os
import csv

csvpath = os.path.join("..", "Resources","budget_data.csv")

total_months = 0
prev_profit = 0
profit_change_list = []
month_of_change_list = []
greatest_inc = ["", 0]
greatest_dec = ["", 999999999999]
total_profit = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

        total_months = total_months + 1
        total_profit = total_profit + int(row[1])

        profit_change =  int(row[1]) - prev_profit
        prev_profit = int(row[1])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change_list = month_of_change_list + [row[0]]

        if (profit_change > greatest_inc[1]):
                greatest_inc[0] = row[0]
                greatest_inc[1] = profit_change

        if (profit_change < greatest_dec[1]):
                greatest_dec[0] = row[0]
                greatest_dec[1] = profit_change

    profit_change_list.pop(0)

    profit_avg = round(sum(profit_change_list) / len(profit_change_list),2)

    output = (
    f"\nFinancial Analysis\n"
    f"\n------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${profit_avg}\n"
    f"Greatest Increase in Profits: {greatest_inc}\n"
    f"Greatest Decrease in Profits: {greatest_dec}\n"
)

print(output)
    

