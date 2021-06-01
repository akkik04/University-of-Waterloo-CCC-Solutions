# 2016 CCC PROBLEM J3'S SOLUTION:

# receiving input as the string.
N = input()

# initially setting the counter for the length of the palindrome to 0.
length_of_palindrome = 0

# creating for-loops to iterate for the length of the string. 
for i in range (0, len(N) + 1):

    for j in range(0, len(N) + 1):
        
        # creating a variable to run through all the indexes from each for-loop.
        palindrome = N[i:j]

        # creating an if-statement to check if the reversed string is the same.
        if palindrome == palindrome[::-1]:
            x = len(palindrome)

            # if the length of the palindrome is larger than the initial set value, rewriting the value.
            if x > length_of_palindrome:

                length_of_palindrome = x

# printing the length of the palindrome.
print(length_of_palindrome)