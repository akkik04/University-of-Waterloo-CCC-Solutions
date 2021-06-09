# 2014 CCC PROBLEM J1'S SOLUTION: 

# receiving input regarding the three angles.
x = int(input())
y = int(input())
z = int(input())

# series of if-statements to determine the characteristics of the triangle.

# determining an equilateral triangle.
if x and y and z == 60:
    print("Equilateral")

# determining an isoceles triangle.
elif (x + y + z == 180) and (x == y or x == z or y == z):
    print("Isoceles")

# determining a scalene triangle.
elif (x + y + z == 180) and (x != y or x != z or y != z):
    print("Scalene")

# printing 'Error' if triangle is not recognized.
else:
    print("Error")
