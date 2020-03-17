#Import a module to create file paths across different operating systems
import os

#Import a module to read and write *.csv files
import csv

#Store the file path
poll_path  = os.path.join("..", "local", "election_data.csv")

#Open the csv file
with open(poll_path) as election_data:
    
    #Initialize the csv reader as file_reader
    file_reader = csv.reader(election_data, delimiter = ",")

    #Read each row in the csv file
    for row in file_reader:
        
        