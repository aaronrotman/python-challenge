#Import modules
#Import a module to create file paths across different operating systems
import os

#Import a module to read and write csv files
import csv

#Assign the file path to a variable
csv_path = os.path.join("..", "local", "budget_data.csv")

#Create an empty list that will store each row of the csv file as its own list within this list
csv_list =[]

#An empty list that will store the change in profit for each month as a list item
change_list = []

#Variabale to store the net profit or loss for the time period covered by this data
net_profit = 0

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

#Read the csv file and append each row of data as a list to a new list
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
        #Append the current month's data as a list to csv_list
        csv_list.append(row)
    
#Calculate the number of months included in the data set
#Count the length of csv_list and assign that value to a variable
data_months = len(csv_list)

#Calculate the month with the greatest incease in profits, and the greatest decrease in profits relative to the previous month
#Iterate through each month of data
for i in range(len(csv_list)):

    #Store the current months profits in a temporary variable
    current_profit = csv_list[i][1]
    #Store the current months date in a temporary variable
    current_date = csv_list[i][0]
    #Store the previous months profits in a temporary variable
    previous_profit = csv_list[i-1][1]
    #Store the current month's change in profits
    profit_change = (current_profit - previous_profit)

    if i == 0:
        pass

    #Check if the current month's change in profits is greater than the previous max increase 'Amount'
    elif profit_change > max_increase['Amount']:
        
        #Set the 'Date' value for max_increase equal to the current month's 'Date'
        max_increase['Date'] = current_date
       
        #Set the 'Amount' value for max_increase equal to the current months's change in profit
        max_increase['Amount'] = profit_change

        #Append the current month's change in profits to change_list
        change_list.append(profit_change)

    #Check if the current month's change in profits is less than the previous max_decrease 'Amount'
    elif profit_change < max_decrease['Amount']:

        #Set the 'Date' value for max_decrease equal to the current month's date
        max_decrease['Date'] = current_date

        #Set the 'Amount' value for max_decrease equal to the current month's change in profits
        max_decrease['Amount'] = profit_change

        #Append the current month's change in profits to change_list
        change_list.append(profit_change)
    
    elif profit_change < max_increase['Amount'] and profit_change > max_decrease['Amount']:
        #Append the current month's change in profits to change_list
        change_list.append(profit_change)
    
    #Add the current months profit value to the net profit counter
    net_profit += current_profit
    

    

#Print out a summary of key metrics
#Print the number of months that the data set covers.
print(f"This analysis covers {data_months} months of data.")

#Print the total net profit for the time period covered by this data
print(f"Total net profit: {net_profit}")

#Print the 'Date' and 'Amount' for the time period with greatest increase in profits
print(f"The greatest increase in profits was in {max_increase['Date']} with a profit of {max_increase['Amount']}")

#Print the 'Date' and 'Amount' for the time period with greatest decrease in profits
print(f"The greatest decrease in profits was in {max_decrease['Date']} with a loss of {max_decrease['Amount']}") 


#Variable to store the sum of the monthly change in profits
sum_change = 0
#Count the number of months of profit change 
num_change = len(change_list)

#Iterate through each month of data
for item in change_list:
    #Stores the current month's change in profits
    current_change = item

    #Calculate the sum of the changes for all months
    sum_change += current_change

#Calculate the mean change for all months
mean_change = sum_change/num_change

#Print the mean change in profits for all months
print(f"Average change: {mean_change}")

#Assign the output path to a variable
output_path = os.path.join("output.txt")

#Open the file in write mode and store the contents in a variable
with open(output_path, 'w') as output_file:
    
    #Initialize the csv writer and specify the delimiter
    csv_writer = csv.writer(output_file, delimiter = ",")

    #Write a title for the summary to the first row
    csv_writer.writerow(["Financial Analysis Summary"])

    #Write the total number of months included in the data to the second row
    csv_writer.writerow([f"Total Number of Months: {data_months}"])

    #Write the total net profit to the third row
    csv_writer.writerow([f"Net Total Profit/Loss: ${net_profit}"])

    #Write the average change in profits to the fourth row
    csv_writer.writerow([f"Mean Change in Profits: ${mean_change}"])

    #Write the greatest increase in profits to the fifth row
    csv_writer.writerow([f"Greatest Increase in Profits: {max_increase['Date']} (${max_increase['Amount']})"])

    #Write the greatest decrease in profits to the sixth row
    csv_writer.writerow([f"Greatest Decrease in Profits: {max_decrease['Date']} (${max_decrease['Amount']})"])