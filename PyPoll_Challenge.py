import csv 
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv") #indirect path
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0
#Candidate options and dictionary to count the votes for each candidate
candidate_options = []
candidate_votes = {}
#County list and dictionary to count the votes for each county
county_options = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Winning Countty and Winning Count per county Tracker
largest_turnout_county = ""
largest_turnout_county_votes_count = 0
largest_turnout_county_votes_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)
      # Read and print the header row.
     headers = next(file_reader)
     # Print each row in the CSV file.

     for row in file_reader:
        #total vote counts
        total_votes += 1
        # Extracts the candidate name from each row
        candidate_name = row[2]
        # Extracts the county name from each row 
        county_name = row[1]
        # Add the candidate name to the candidate list if it isn't already in the list
        if candidate_name not in candidate_options: 
            # Add the candidate name
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1     

        if county_name not in county_options:
            # Add the county name
            county_options.append(county_name)
            #Begin tracking that candidate's vote count.
            county_votes[county_name] = 0

        # Add a vote to that candidate's count.
        county_votes[county_name] += 1       


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        county_results = (f"{county_name}:  {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)

        if (votes>largest_turnout_county_votes_count) and (vote_percentage>largest_turnout_county_votes_percentage):
            largest_turnout_county_votes_count=votes
            largest_turnout_county_votes_percentage=vote_percentage
            largest_turnout_county = county_name

    # Print the largest turnout county (to terminal)
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout_county}\n"
        f"-------------------------\n")

    print(winning_county_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_county_summary)


    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

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
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)