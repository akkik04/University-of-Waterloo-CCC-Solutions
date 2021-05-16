# 2020 CCC PROBLEM J1'S SOLUTION:

# declaring variables for the treat sizes.
SMALL_TREATS = int(input())
MEDIUM_TREATS = int(input())
LARGE_TREATS = int(input())

# arithmetic calculation for the determinant.
determinant = (1 * SMALL_TREATS) + (2 * MEDIUM_TREATS) + (3 * LARGE_TREATS)

# determining whether the dog is happy based on the determinant.
if determinant >= 10:
    print("happy")

else: 
    print("sad")