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
        
        #Print the current row
        #print(row)

        #Append the temporary list to csv_list
        csv_list.append(row)

    #Loop through each list in csv_list
    for list in csv_list:
        
        #print(list)
        #print(f"Column 1 type: {type(list[0])}")
        #print(f"Column 2 type: {type(list[1])}")

        #Check if the current list's 'Amount' value is greater than max_increase
        if int(list[1]) > int(max_increase['Amount']):
            
            #Set the max_increase 'Date' value to the current list's 'Date' value
            max_increase['Date'] = list[0]
            #print(max_increase['Date'])
            
            #Set the max_increase 'Amount' value equal to the current list's 'Amount' value
            max_increase['Amount'] = int(list[1])
            #print(max_increase['Amount'])

        #Check if the current list's 'Amount value is less than max_increase
        elif int(list[1]) < int(max_decrease['Amount']):
            
            #Set the max_decrease 'Date' value to the current list's 'Date' Value
            max_decrease['Date'] = list[0]
            #print(max_decrease['Date'])

            #Set the max_decrease 'Amount' value to the current list's 'Amount' value
            max_decrease['Amount'] = int(list[1])
            #print(max_decrease['Amount'])
        
        elif int(list[1]) == max_increase['Amount']:
            print("Uh oh! There are multiple values for max_increase")
        
        elif int(list[1]) == max_decrease['Amount']:
            print("Uh oh! There are multiple values for max_decrease")

    #Print the 'Date' and 'Amount' for the time period with greatest increase in profits
    print(f"The greatest increase in profits was in {max_increase['Date']} with a profit of {max_increase['Amount']}")

    #Print the 'Date' and 'Amount' for the time period with greatest decrease in profits
    print(f"The greatest decrease in profits was in {max_decrease['Date']} with a loss of {max_decrease['Amount']}") 
    
#Store the first date in a variable
first_date = csv_list[0][0]
print(f"First date: {first_date}")

#Store the last date in a variable
last_date = csv_list [-1][0]
print(f"Last Date: {last_date}")

#Calculate the number of months included in the data set
data_months = len(csv_list)
print(f"This analysis covers {data_months} months of data.")


