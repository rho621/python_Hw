import os
import csv

csvpath = os.path.join("..", "Resources","election_data.csv")
file_out = "..", "Resources", "ouput.txt"

total_voters = 0
candi_list = []
cand_vote = {}
cand1_per = 0
cand2_per = 0
cand3_per = 0
cand4_per = 0

winning_candi = ""
winning_count = 0



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        total_voters = total_voters + 1

        cand_name = row[2]

        if cand_name not in candi_list:
            candi_list.append(cand_name)

            cand_vote[cand_name] = 0

        cand_vote[cand_name] = cand_vote[cand_name] + 1
            
    election_results = (
        f"\n\nElection Resuts\n"
        f"--------------------\n"
        f"Total Votes: {total_voters}\n"
        f"---------------------\n"
        )

    print(election_results)
    
    for candi in cand_vote:
        
        votes = cand_vote.get(candi)
        vote_percent = round(float(votes) / float(total_voters) * 100, 4)

        if (votes > winning_count):
            winning_count = votes
            winning_candi = candi

        winner_info = (
            f"----------------------\n"
            f"Winner: {winning_candi}\n"
            f"----------------------\n"
        )

        voter_ouput = (
            f"{candi}: {vote_percent}:% ({votes})\n"
        )  

        print(voter_ouput)
    print(winner_info)










        
       




        

    

    


        

