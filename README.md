# Election Analysis


Overview of Election Audit:
We were asked Tom, an employee for the Colorado board of elections, to create a code that can be used for an election audit of tabulated voter data. Tom needed us to report the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on popular vote. As well as, county data for the election: votes from each county, percentage of votes from each county, and which county voted most.


Election-Audit Results:
Through our audit we found that 369,711 total votes were cast in this election. Of the 3 counties that voted, we found the following data:

County Votes:
Jefferson:10.5% 38,855
Denver:82.8% 306,055
Arapahoe:6.7% 24,801

Here you can see that Denver county accounted for most of the votes, over 80%. While Jefferson and Arapahoe county had much less voters.
The results for the election are as follows:

Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

We can see that Diana DeGette won this election by a landslide. She had 272,892 voters, accounting for almost 3/4 of all votes!


Election Audit Summary:
I would like to propose that the code we created: "PyPoll_Challenge_code.py", be used for future elections as well. The code we created can actually be used for any election with a few modifications. So long as we have a similarily formatted .csv file of voter data, this code will report the winning candidate, as well as voting data. The only modification in the code itself will be in line 9:

file_to_load = os.path.join("resources", "election_results.csv")

This is where the code links to the election results specific to this election. For a future election audit, we would just have to change this line to reference the data in whatever new file we are using. 

Another minor change that may need to occur is changing the values in our lines 48-52 of code:

# Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
  
Here we created variables to hold the values of the .csv file. The column in index 1 in the .csv file contained the name of the county for each individual voter. So we set the data in the index to be held in the variable "county name". The column in index 2 of the .csv file contained the candidate name of the candidate the individual voted for. So we created the variable "candidate name" to hold the data of which candidate voters voted for. 

If a future voting data .csv file was formatted with this data in different indices, (for example, candidate name being in index 1 and county name being stored in index 2) we would need to edit this code to reference the appropriate date in our csv file.
