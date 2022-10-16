import csv 
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv") #indirect path
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0
#Candidate options
candidate_options = []
#Dictionary to count the votes for each candidate
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)
      # Read and print the header row.
     headers = next(file_reader)
     #print(headers)
     # Print each row in the CSV file.
     for row in file_reader:
          total_votes += 1
          # Print the candidate name from each row
          candidate_name = row[2]
          # Add the candidate name to the candidate list if it isn't already in the list
          if candidate_name not in candidate_options: 
               # Add the candidate name
               candidate_options.append(candidate_name)
               #Begin tracking that candidate's vote count.
               candidate_votes[candidate_name] = 0

          # Add a vote to that candidate's count.
          candidate_votes[candidate_name] += 1         

for candidate_name in candidate_votes:
     votes = candidate_votes[candidate_name]
     vote_percentage = float(votes)/float(total_votes) * 100
     #Used to print the candidate and the percentage of votes
     print(f"{candidate_name}:  {vote_percentage:.2f}% ({votes:,})\n")

     if (votes>winning_count) and (vote_percentage>winning_percentage):
          winning_count=votes
          winning_percentage=vote_percentage
          winning_candidate = candidate_name
         
winning_candidate_summary = (
    f"-------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"-------------------------\n")

print(winning_candidate_summary)    
     


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Counties in the Election\n")
     txt_file.write("-------------------------\n")
     txt_file.write("Arapahoe \nDenver \nJefferson")
