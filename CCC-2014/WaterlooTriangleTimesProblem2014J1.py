# 2014 CCC PROBLEM J1'S SOLUTION: 

# receiving input regarding the three angles.
x = int(input())
y = int(input())
z = int(input())

# series of if-statements to determine the characteristics of the triangle.
if x and y and z == 60:
    print("Equilateral")

elif (x + y + z == 180) and (x == y or x == z or y == z):
    print("Isoceles")

elif (x + y + z == 180) and (x != y or x != z or y != z):
    print("Scalene")

else:
    print("Error")