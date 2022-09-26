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


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # read and analyze data
    file_reader = csv.reader(election_data)
    #for row in file_reader:
     #   print(row)
    headers = next(file_reader)
    print(headers)







#file_to_save = os.path.join("analysis","election_analysis.txt")
#pen(file_to_save,"w")

#use the open statement to open the file as a text file
#with open(file_to_save,"w") as txt_file:


#write some data to the file
#    txt_file.write("Counties in the Election\n----------\nArapahoe\nDenver\nJefferson")




