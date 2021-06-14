# 2014 CCC PROBLEM J2'S SOLUTION: 

# creating variables to store the input.
num_votes = int(input())
characters = input()

# creating two variables to store the values for A-votes and B-votes.
votes_A = 0
votes_B = 0

# creating a for-loop to iterate for the length of the string.
for i in range(0, len(characters)):
    
    # creating an if-statement to check for each vote and increment the A-votes or B-votes.
    if characters[i: i + 1] == 'A'.upper():
        votes_A += 1

    elif characters[i: i + 1] == 'B'.upper():
        votes_B += 1

# creating an if-statement to determine if 'A' or 'B' has more votes.
if votes_A > votes_B:
    print("A")

elif votes_A < votes_B:
    print("B")

else:
    print("Tie")