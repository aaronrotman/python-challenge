#Import modules

#Import a module to create file paths across different operating systems
import os

#Import a module to read and write csv files
import csv

#Assign the file path to a variable
csv_path = os.path.join("..", "local", "budget_data.csv")

with open(csv_path) as csv_file:

    #Select the delimiter and choose a variable to store that selection
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Read each row in the csv file
    for row in csv_reader:
        #Print the current row
        print(row)
  