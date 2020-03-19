#Import modules

#Import a module to create file paths across different operating systems
import os

#Import a module to read and write csv files
import csv

#Assign the file path to a variable
csv_path = os.path.join("..", "local", "budget_data.csv")

#Create an empty list that will store each row of the csv file as its own list within this list
csv_list =[]

#Create a dictionary to store 'Date' and 'Amount' for the month with the greatest increase in profits
max_increase = {
    #Set 'Amount' to start at 0
    'Amount': 0,
    
}

#Create a dictionary to store 'Date' and 'Amount' for the month with the greatest decrease in profits
max_decrease = {
    #Set 'Amount to start at 0
    'Amount': 0,
}

with open(csv_path) as csv_file:

    #Assign a variable to store the csv.reader object
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Assign the header row to a variable
    csv_header = next(csv_reader)
    #print(csv_header)

    #Read each row in the csv file
    for row in csv_reader:
        
        #Change the current row 'Amount' type to integer
        row[1] = int(row[1])
  
        csv_list.append(row)
        
#Store the first date in a variable
first_date = csv_list[0][0]
print(f"First date: {first_date}")

#Store the last date in a variable
last_date = csv_list [-1][0]
print(f"Last Date: {last_date}")


#Calculate the number of months included in the data set

#Count the length of csv_list and assign that value to a variable
data_months = len(csv_list)
print(f"This analysis covers {data_months} months of data.")


#Calculate the month with the greatest increase in profits relative to the previous month


#Iterate through each list in csv_list
for i in range(len(csv_list)):

    #Store the current months profits in a temporary variable
    current_profit = csv_list[i][1]
    current_date = csv_list[i][0]
    #Store the previous months profits in a temporary variable
    previous_profit = csv_list[i-1][1]
    profit_change = (current_profit - previous_profit)

    #print(f"Current Date: {current_date} Current profit: {current_profit} Previous Profit: {previous_profit} Profit Change: {profit_change}")


    #Check if the current month's change in profits is greater than the previous max increase 'Amount'
    if profit_change > max_increase['Amount']:
        
        #Set the 'Date' value for max_increase equal to the current month's 'Date'
        max_increase['Date'] = current_date
        #print(max_increase['Date'])
        
        #Set the 'Amount' value for max_increase equal to the current months's change in profit
        max_increase['Amount'] = profit_change
        #print(max_increase['Amount'])

    #Check if the current month's change in profits is less than the previous max_decrease 'Amount'
    elif profit_change < max_decrease['Amount']:

        #Set the 'Date' value for max_decrease equal to the current month's date
        max_decrease['Date'] = current_date

        #Set the 'Amount' value for max_decrease equal to the current month's change in profits
        max_decrease['Amount'] = profit_change
        
    
#Print the 'Date' and 'Amount' for the time period with greatest increase in profits
print(f"The greatest increase in profits was in {max_increase['Date']} with a profit of {max_increase['Amount']}")

#Print the 'Date' and 'Amount' for the time period with greatest decrease in profits
print(f"The greatest decrease in profits was in {max_decrease['Date']} with a loss of {max_decrease['Amount']}") 

