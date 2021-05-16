# 2021 CCC PROBLEM J2'S SOLUTION:

# declaring necessary variables.
number_of_bids = int(input())
winner_name = ' '
highest_bid = 0

# for-loop to iterate for the amount of bid's placed.
for i in range(number_of_bids):

    # receiving the individual's name and their corresponding bid.
    person_name = input()
    bid_amount = int(input())

    # if-statement to determine the winner.
    if bid_amount > highest_bid:
        winner_name = person_name
        highest_bid = bid_amount

# printing the winner's name.
print(winner_name)