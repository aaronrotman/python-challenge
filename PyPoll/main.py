#Import a module to create file paths across different operating systems
import os

#Import a module to read and write *.csv files
import csv

#Store the path of the file to read
poll_path  = os.path.join("Resources", "election_data.csv")

#Store the output path to write to
output_path = os.path.join("election_results.txt")

#Empty list to store the name of the candidate selected for each vote
votes_cast = []

#Empty list to store the name of each unique candidate who received a vote
unique_list = []

#Open the csv file
with open(poll_path) as election_data:

    #Initialize the csv reader as file_reader
    file_reader = csv.reader(election_data, delimiter = ",")
    #Assign the first row to a variable as the header
    header_row = next(file_reader)
    
    #Read each row in the csv file
    for row in file_reader:
        #Assign the candidates name to a variable
        candidate_name = row[2]
     
        #Check if the candidates name is already in the list of unique names
        if candidate_name in unique_list:
            #Add the candidate's name to the list of votes
            votes_cast.append(candidate_name)
        
        #Check if the candidates name if not in the list of unique names    
        elif candidate_name not in unique_list:
            #Add the candidate's name to the list of votes
            votes_cast.append(candidate_name)
            #Add the candidate's name to the list of unique names
            unique_list.append(candidate_name)
            

  


#List to store the names and number of votes for each candidate
results_list = []

#Iterate through each candidate in the list of unique candidates
for candidate in unique_list:
    #Count the number of times the candidate appeared in the list of votes cast
    vote_count = votes_cast.count(candidate)
    #create a temporary list to the candidates name and vote count
    candidate_info = [candidate, vote_count]
    #Append the list of containing the candidates name and vote count to the results list
    results_list.append(candidate_info)


#Determine which candidate received the most votes
#Variable to store the total number of votes cast
total_votes = len(votes_cast)  

#Print out a summary of the election results

#Print the total number of votes cast
print(f"Total Votes: {total_votes}")  

#Variable to store the highest number of votes received by a single candidate
most_votes = 0
#Variable to store the name of the candidate who received the highest number of votes
winner = ""

#Print the name and number of votes for each candidate
#Iterate through each candidate who received a vote
for result in results_list:
    #Print the candidates name and number of votes received
    print(f"{result[0]}: {result[1]}")
    #check if this candidate received more votes than the current high number
    if result[1] > most_votes:
        #Assign the current candidates value to the most votes variable
        most_votes = result[1]
        #Assign the current candidates name to the winner variable
        winner = result[0]

#Print the name and vote count of the winning candidate
print(f"The winner is: {winner} with {most_votes} votes!")


#Write the election results to a new text file 
#Open the output file in write mode and assign the contents to a variable
with open(output_path, "w") as results_file:
    
    #Initialize the csv writer and assign the writer to a variable
    file_writer = csv.writer(results_file, delimiter = ",")
    
    #Write the total number of votes to the summary text file
    file_writer.writerow([f"Total Votes: {total_votes}"])

    #Iterate through each candidate in the list of results
    for result in results_list:
        #Write the name and number of votes for this candidate to the summary text file
        file_writer.writerow([f"{result[0]}: {result[1]}"])

    #Write the winner's name and vote count to the summary text file
    file_writer.writerow([f"The winner is: {winner} with {most_votes} votes!"])