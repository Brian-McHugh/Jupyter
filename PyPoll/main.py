# Calculate total number of votes cast in election_data.csv
# Three columns: Voter ID, County, Candidate

# Import dependencies
import os
import csv

# Specify the path to access our data
csv_path = os.path.join("Resources", "election_data.csv")

# Create lists for each category/column of the csv
voterIDs = []
counties = []
votes = []

# Open and read the csv file
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Read the header row
    csv_header = next(csv_reader)
    
    # Fill our lists with data
    for voterID, county, candidate in csv_reader:
        voterIDs.append(voterID) #might need to change to int
        counties.append(county)
        votes.append(candidate)

# Create a list of candidates who received votes
candidates = []
for candidate in votes:
    if candidate not in candidates:
        candidates.append(candidate)
        
#print(candidates)

# Total votes cast for all candidates
total_votes = len(voterIDs)

# Vote totals for each candidate
khan_count = votes.count("Khan")
correy_count = votes.count("Correy")
li_count = votes.count("Li")
otooley_count = votes.count("O'Tooley")

# Percentage of total votes for each candidate
khan_perc = round(khan_count / total_votes * 100)
correy_perc = round(correy_count / total_votes * 100)
li_perc = round(li_count / total_votes * 100)
otooley_perc = round(otooley_count / total_votes * 100)

# Check for the winner of the election
candidates_ = {"Khan": khan_count, "Correy": correy_count, "Li": li_count, "O'Tooley": otooley_count}
winner = max(candidates_, key=candidates_.get)
#print(winner, "is the winner")

def analysis():
    print("Election Results")
    print("-"*25)
    print(f"Total Votes: {total_votes}")
    print("-"*25)
    print(f"Khan: {khan_perc}% ({khan_count})")
    print(f"Correy: {correy_perc}% ({correy_count})")
    print(f"Li: {li_perc}% ({li_count})")
    print(f"O'Tooley: {otooley_perc}% ({otooley_count})")
    print("-"*25)
    print(f"Winner: {winner}")
    print("-"*25)

# Print analysis to terminal
analysis()

# Specify the file to write to
output_file = "election_data.txt"

with open(output_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-"*25 + "\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-"*25 + "\n")
    outfile.write(f"Khan: {khan_perc}% ({khan_count})\n")
    outfile.write(f"Correy: {correy_perc}% ({correy_count})\n")
    outfile.write(f"Li: {li_perc}% ({li_count})\n")
    outfile.write(f"O'Tooley: {otooley_perc}% ({otooley_count})\n")
    outfile.write("-"*25 + "\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-"*25 + "\n")

