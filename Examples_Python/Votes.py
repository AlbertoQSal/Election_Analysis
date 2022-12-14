counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

# Using traditional concatenation 
for county, voters in counties_dict.items():

    print(county + " county has " + str(voters) + " registered voters.")

print("\n")

# Using f-string
for county, voters in counties_dict.items():

    print(f"{county} county has {voters:,} registered voters. ")

print("\n")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
