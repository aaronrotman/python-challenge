#Import a module to create file paths across different operating systems
import os

#Import a module to read and write *.csv files
import csv

#Store the file path
poll_path  = os.path.join("..", "local", "election_data.csv")

#list[index][key] += 1

#Empty list to store the name of the candidate selected for each vote
candidate_list = []

#Empty list to store the name of each unique candidate who received a vote
unique_list = []

#Variable to store the total number of votes cast in the election
total_votes = 0

#Open the csv file
with open(poll_path) as election_data:

    #Initialize the csv reader as file_reader
    file_reader = csv.reader(election_data, delimiter = ",")
    #Assign the first row to a variable as the header
    header_row = next(file_reader)
    #Print the header row
    #print(header_row)
    
    #Read each row in the csv file
    for row in file_reader:
        #Assign the candidates name to a variable
        candidate_name = row[2]
        #print(candidate_name)
        #print(row)
        #print(candidate_list)
        
        #Append the candidates name to a new list
        #candidate_list += candidate_name
        if candidate_name in unique_list:
            candidate_list.append(candidate_name)
            #print(f"Unique List: {unique_list}")
        elif candidate_name not in unique_list:
            #print(candidate_name)
            candidate_list.append(candidate_name)
            unique_list.append(candidate_name)
            #print(unique_list)
        
print(unique_list)
print(len(candidate_list))     
#print(candidate_list[0]) 
#print(candidate_list[-1])
#print(total_votes)