# 2015 CCC PROBLEM J1'S SOLUTION:

def calc_special_day(month, day_of_the_month):

    # if-statement to determine the special day.
    if (month == 2) and (day_of_the_month == 18):
        return 'Special'

    elif (month > 2) and (day_of_the_month > 18):
        return 'After'

    else:
        return 'Before'

# code to receive the value for the month and the day of the month.
month = int(input())
day_of_the_month = int(input())

# code to print the output of the day.
print(calc_special_day(month, day_of_the_month))