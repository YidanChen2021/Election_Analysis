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

with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    print(headers)