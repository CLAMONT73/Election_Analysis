# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Election_Analysis","Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options.
candidate_options = []
# ADDED: County Options.
county_name = []
# Declare the empty dictionary.
candidate_votes = {}
# ADDED: Declare a county votes dictionary.
county_votes = {}
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
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add to the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to candidate's count.
        candidate_votes[candidate_name] += 1
    # ADDED: County list and votes for each.    
    for row in file_reader:
        county_votes += 1
        county_name = row[1]
        if county_name not in county_name:
            county_name.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")     
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)     
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
    # Save the candidate results to our text file.
    txt_file.write(candidate_results)
    # Determine winning vote count, winning percentage, and winning candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_candidate = candidate
        winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    # Removing this write statement prevents from writing candidate summary to the text file, even though "county_results" gets assigned below in line 95.
    txt_file.write(county_results)   
    # Close the text file. 
    txt_file.close()
    # ADDED:
with open(file_to_save, "w") as txt_file:
    county_results = (
        f"\nCounty Votes:\n"
        f"{county_name}: {county_percentage:.1f}% ({covotes:,})\n")
     # ADDED: County votes and percentage.
    for county in county_votes:
        covotes = county_votes[county]
        county_percentage = float(county_percentage) / float(total_votes) * 100
        county_results = (f"{county_name}: {county_percentage:.1f}% ({covotes:,})\n")
    print(county_results)
    txt_file.write(county_results)        
    # ADDED: Save the county results to our text file.

    # Close the text file.
    txt_file.close()
# Close the CSV file.
election_data.close()