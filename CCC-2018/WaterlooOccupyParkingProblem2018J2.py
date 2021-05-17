# 2018 CCC PROBLEM J2'S SOLUTION: 

# declaring variables to store various values corresponding to the program.
num_of_parking_spaces = int(input())

yesterdays_input = input()
todays_input = input()

# declaring a variable to store the count of the same spaces.
same_spaces = 0

# for-loop to iterate for the amount of parking spaces.
for i in range(0, num_of_parking_spaces):

    # nested if-statement to determine how many of the same spaces are occupied on each day.
    if (yesterdays_input[i] == 'C' and todays_input[i] == 'C'):
        same_spaces += 1

# code to print the final output indicating how many of the same spaced were occupied on each day.
print(same_spaces)