# 2018 CCC PROBLEM J1'S SOLUTION: 

# declaring variables to store the values for the last 4 digits of the phone number.
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# if-statement to determine if we should pick up the call based on the last 4 digits' characteristics.
if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3):
    print("ignore")

else:
    print("answer")