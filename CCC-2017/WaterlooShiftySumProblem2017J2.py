# 2017 CCC PROBLEM J2'S SOLUTION:

def shifty_sum(number_to_shift, num_of_shifts, sum):

    # creating a for-loop that iterates for the number of shifts that the user specified.
    for i in range(num_of_shifts):
        
        # calculating the shifty sum.
        number_to_shift = number_to_shift * 10
        sum = sum + number_to_shift
    
    # returning the shifty sum.
    return (sum)

# declaring variables to store values for the inital number and the number of shifts required.
number_to_shift = int(input())
num_of_shifts = int(input())

# declaring a variable to store the value of the sum.
sum = 0
sum = sum + number_to_shift

# code to print out the shifty sum to the user.
print(shifty_sum(number_to_shift, num_of_shifts, sum))