def find_Voter():
    voter_age=int(input("age of voter:"))
    if voter_age>18:
        print("voter has right to vote in election")
    if voter_age<18:
        print("voter is minor and does not have right to vote in election")
find_Voter()
