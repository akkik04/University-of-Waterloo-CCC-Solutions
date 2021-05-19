# 2016 CCC PROBLEM J1'S SOLUTION:

# creating a variable to store the number of wins.
counter = 0

# creating a for-loop to iterate for the range of the input.
for i in range(0, 6):
    
    letters = input()

    # nested if-statement to increase the counter for every win.
    if letters == 'W':
        counter += 1

# if-statement to determine which group the player falls into.klk
if counter == 0:
    print("-1")

elif counter == 1 or counter == 2:
    print("3")

elif counter == 3 or counter == 4:
    print("2")

else:
    print("1")