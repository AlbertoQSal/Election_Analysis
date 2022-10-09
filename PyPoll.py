import csv 
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv") #indirect path
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)
      # Read and print the header row.
     headers = next(file_reader)
     print(headers)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Counties in the Election\n")
     txt_file.write("-------------------------\n")
     txt_file.write("Arapahoe \nDenver \nJefferson")
