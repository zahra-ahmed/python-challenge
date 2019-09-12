import os
import csv

# file path
poll_csv = os.path.join('election_data.csv')

# create lists to put csv data into
votes_list = []
candidates_list = []
final_candidates = []

# Read in the CSV file
with open(poll_csv, newline='') as csvfile:

    # Split the data on commas and identify headers
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # take data from csv file and put into lists
    for row in csvreader:
        
        votes_list.append(row[0])

        candidates_list.append(row[2])

# total number of votes cast
total_votes = len(votes_list)

# list of all candidates who got votes
for x in range(len(candidates_list)):
    if candidates_list[x] not in final_candidates:
        final_candidates.append(candidates_list[x])



# percentage of votes candidates won
percentages = []
for x in range(len(final_candidates)):
    percentages.append(candidates_list.count(str(final_candidates[x]))/total_votes * 100)



#total number of votes candidates won
candidate_votes = []
for x in range(len(final_candidates)):
    candidate_votes.append(candidates_list.count(str(final_candidates[x])))



# determine the winner
winner = str(final_candidates[0])
for x in range(len(candidate_votes)-1):
    if candidate_votes[x+1] > candidate_votes[x]:
        winner = str(final_candidates[x+1])


        


print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
for x in range(len(final_candidates)):
    print(f"{final_candidates[x]}: {percentages[x]}% ({candidate_votes[x]})")
print(f"---------------------------")
print(f"Winner: {winner}")
print(f"---------------------------")


# write into txt file

#file path
text_file = os.path.join('election_results.txt')

with open(text_file, 'w') as text:
    text.write(f"Election Results\n")
    text.write(f"---------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write(f"---------------------------\n")
    for x in range(len(final_candidates)):
        text.write(f"{final_candidates[x]}: {percentages[x]}% ({candidate_votes[x]})\n")
    text.write(f"---------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write(f"---------------------------\n")
    




