# 2019 CCC PROBLEM J1'S SOLUTION: 

# declaring variables to store input for the apples team.
three_point_apples = int(input())
two_point_apples = int(input())
one_point_apples = int(input())

# declaring variables to store input for the bananas team.
three_point_bananas = int(input())
two_point_bananas = int(input())
one_point_bananas = int(input())

# arithmetic calculation to determine the sum of points for both of the teams.
sum_points_apple = (3 * three_point_apples) + (2 * two_point_apples) + one_point_apples
sum_points_bananas = (3 * three_point_bananas) + (2 * two_point_bananas) + one_point_bananas

# if-statement to determine which team has more points.
if sum_points_apple > sum_points_bananas:
    print("A")

elif sum_points_bananas > sum_points_apple:
    print("B")

else:
    print("T")