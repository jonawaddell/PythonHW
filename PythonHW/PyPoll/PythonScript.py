import os
import csv
import collections

vote_id = []
county = []
candidate = []
candiateReader = []
candidateVotes = {}
CandidateResult = 0


#Path to collect data from the Resources folder
election_data_1 = os.path.join('election_data_1.csv')
file_to_output = file_to_output = 'election_data_1.txt'
 
#Define the function and have it accept the 'exercise_data_1' as its sole parameter
with open(election_data_1, newline="") as data1:
    csv_reader = csv.reader(data1, delimiter=",")
    next(csv_reader, None)
#-----------------------------------------------------
#The total number of votes cast
    print ("Election Results")
    print("-------------------------")
    row_count = sum(1 for row in data1)
    print(row_count)
    print("-------------------------")
#-----------------------------------------------------
   #align the variables with columns
    for rows in csv_reader:
        vote_id.append(rows[0])
        county.append(rows[1])
        candidate.append(rows[2])
        #get list of candiate(no duplicate) and get total votes
        if candidate not in candiateReader:
           candiateReader.append([candidate]) 
           candidateVotes[[candidate]] = 1
           
        else:
            candidateVotes[rows["candidate"]] = candiateVotes[rows["candidate"]] + 1
            
 #------------------------------------------------------
         for candidate in candidateVotes:
             print(candidate + " " + str(round(((candidateVotes[candidate]/vote_id)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
             CandidateResult = (candidate + " " + str(round(((candidateVotes[candidate]/vote_id)*100))) + "%" + " (" + str(candidateVotes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")
            
        
with open(file_to_output, w, newline="") as CsvFile:
    csvwriter = csv.writer(CsvFile, delimiter=",")
    csvwriter.writerrows()        
        
                

                
        
    
