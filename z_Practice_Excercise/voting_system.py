



def voting_system():
    candidates = ["Alice", "Bob", "Charlie"]
    votes = {"Alice": 0, "Bob": 0, "Charlie": 0}

    while True:
        print("Candidates:", candidates)
        vote = input("Enter your vote (or type 'exit' to stop voting): ")

        if vote == "exit":
            print("Thank you for voting, goodbye")
            break

        
        if vote in candidates:
            votes[vote] += 1
        else:
            print("Invalid vote !! please choose a valid candidates")


    return votes


print(voting_system())
