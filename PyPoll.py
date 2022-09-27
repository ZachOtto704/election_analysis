# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of canidates who recieved votes
#3. The percentage of votes each canidate won
#4. The total number of votes each canidate one
#5. The winner of the election based on popuar vote

#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#create a list to hold canidates
candidate_options = []

#create an empty dictionary to hold candidate votes
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # read and analyze data
    file_reader = csv.reader(election_data)
   
   #read the header row
    headers = next(file_reader)
    print(headers)

    #print each row in csv file
    for row in file_reader:
        #increase total vote count
        total_votes += 1

        #get candidate name from each row
        candidate_name = row[2]

        #If name does not match an already existing value in options...
        if candidate_name not in candidate_options:

            #add to list of candidates  
            candidate_options.append(candidate_name)    

            #initialize candidate names as the key to votes dictionary
            candidate_votes[candidate_name]=0

        #add vote to candidate count
        candidate_votes[candidate_name] += 1

    #save the results to our text file
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
        
        #save final vote count to text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
            
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
            #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
            #print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

            #determine if the votes is greater than winning total
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count=votes
                winning_percentage=vote_percentage
                winning_candidate=candidate_name

    winning_candidate_summary=(
            f"---------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"----------------\n")

    print(winning_candidate_summary)    

    txt_file.write(winning_candidate_summary)



        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    #print candidate list
    #print(candidate_votes)












    #file_to_save = os.path.join("analysis","election_analysis.txt")
    #pen(file_to_save,"w")

    #use the open statement to open the file as a text file
    #with open(file_to_save,"w") as txt_file:


    #write some data to the file
    #    txt_file.write("Counties in the Election\n----------\nArapahoe\nDenver\nJefferson")




