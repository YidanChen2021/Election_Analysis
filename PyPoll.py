#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidates won
#4. The total number of votes each candidates won
#5. The winner of the election based on popular vote.

#Assign a Variable for the file to load and the path
file_to_load = '.\Resources\election_results.csv'
#Open the election results and read the file
election_data = open(file_to_load, 'r')
# To do: perform analysis

# Close the file
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: Perform analysis
    print(election_data)

import os
import csv
file_to_load = os.path.join("Resources","election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)

#Create a filename variable or indirect path to the file.
file_to_save = os.path.join("analysis", "eletion_analysis.txt")
#Use the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    #Write the three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")

#1. initialize a total vote counter
total_votes = 0

#Candidate oprtions and candidate votes
Candidate_options = []
#1. Declare the empty dictionary
Candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    print(headers)
    
    #Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        #Print Candidate name from each row
        Candidate_name = row[2]
        # If the candidate doesn not match any existing candidate...
        if Candidate_name not in Candidate_options:
            # Add the Candidate name to the candidate list
            Candidate_options.append(Candidate_name)
            #2. Begin tracking that candidate's vote count.
            Candidate_votes[Candidate_name] = 0
        # Add a vote to that candidate's count
        Candidate_votes[Candidate_name] += 1
with open(file_to_save,"w") as txt_file:       
#Print the final vote count to the terminal
    election_result = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"---------------------------\n")
    print(election_result, end="")
    #Save the final Vote Count to the test file
    txt_file.write(election_result)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in Candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = Candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        Candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(Candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(Candidate_results)
        #1. Determine if the votes are greater than the winning count.
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            #2. If true thn set winning_count =  votes and winning_percentage = vote_percentage
            winning_count=votes
            winning_percentage=vote_percentage
            #3. Set the winning_candidate name equal to the candidate's name.
            winning_candidate=Candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

    