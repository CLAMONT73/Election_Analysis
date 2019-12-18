'''
CHALLENGE INSTRUCTIONS: Make a copy of PyPoll.py and rename to PyPoll_Challenge.py.
Create a list for the counties / Create a dictionary where the county is the key
and votes for each are the values / Create an empty string that will hold the county
name with the largest turnout / Declare a variable that represent the # of votes a
county received / Inside the with open(): Create if statements to print voter turnout /
Add results to output file / Print results to the command line.
'''

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options.
candidate_options = []

# ADDED: County Options.
county_options = []

# Declare the empty dictionary.
candidate_votes = {}

# ADDED: Declare a county votes dictionary.
county_votes = {}

total_county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# ADDED: Track county with largest turnout.
largest_turnout = ""
largest_count = 0
largest_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file and add to the total vote count.
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # And begin tracking candidate's voter count.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        # CHALLENGE: Added county list and votes for each.
        county_name = row[1]

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
     election_results = (
         f"\nElection Results\n"
         f"-------------------------\n"
         f"Total Votes: {total_votes:,}\n"
         f"-------------------------\n")
     print(election_results, end="")    
               
     txt_file.write(election_results)

     county_headers = (
         f"\nCounty Votes:\n")
     print(county_headers)

     txt_file.write(county_headers)

    # CHALLENGE: Added county votes.
     for county in county_votes:
        covotes = county_votes[county]
        county_percentage = float(covotes) / float(total_votes) * 100
        county_results = (
            f"{county}: {county_percentage: .1f}% ({covotes:,})\n")

        print(county_results)

        txt_file.write(county_results)

        # CHALLENGE: Added largest turnout details.
        if covotes > largest_count:
            largest_count = covotes
            largets_turnout = county
            largest_percentage = county_percentage

    # Print to the terminal.
     largest_county_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")  

     print(largest_turnout)

     txt_file.write(largest_county_turnout)   

     for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

    # Determine winning vote count, percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

        txt_file.write(candidate_results)    
    
     winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
     print(winning_candidate_summary)

     txt_file.write(winning_candidate_summary)