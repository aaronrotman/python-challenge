#Import modules

#Import a module to create file paths across different operating systems
import os

#Import a module to read and write csv files
import csv

#Assign the file path to a variable
csv_path = os.path.join("..", "local", "budget_data.csv")

#Create an empty list that will store each row of the csv file as its own list within this list
csv_list =[]

with open(csv_path) as csv_file:

    #Select the delimiter and choose a variable to store that selection
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header = next(csv_reader)
    print(csv_header)

    #Read each row in the csv file
    for row in csv_reader:
        
        #Append the temporary list to csv_list
        csv_list.append(row)
        
        #Print the current row
        #print(row)

    for list in csv_list:
        print(list)

first_date = csv_list[0][0]
last_date = csv_list [-1][0]
print(f"First date: {first_date}")
print(f"Last Date: {last_date}")