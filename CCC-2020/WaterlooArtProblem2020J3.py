# receiving input.
N = int(input())

# creating an array to store the coordinates.
colour_drops = []

# creating a for-loop to iterate for 'N'
for i in range (N):

    # creating an object.
    drop = {}

    # receiving input regarding the coordinates.
    drop_input = list(map(int, input().split(',')))

    # storing the values of 'x' and 'y' in the object.
    drop['x'] = drop_input[0]
    drop['y'] = drop_input[1]

    # appending the coordinates to the array.
    colour_drops.append(drop)

# setting the default values for min and max x, y.
min_x = None
max_x = None
min_y = None
max_y = None

# creating a for-loop to iterate for the array.
for points in colour_drops:
    x = points['x']
    y = points['y']

    # creating an if-statement to compare the values to find the smallest possible rectangle.
    if not min_x or x < min_x:
        min_x = x
    if not max_x or x > max_x:
        max_x = x
    if not min_y or y < min_y:
        min_y = y
    if not max_y or y > max_y:
        max_y = y

# printing the expected output.
print(str(min_x - 1) + "," + str(min_y - 1))
print(str(max_x + 1) + "," + str(max_y + 1))