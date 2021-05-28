# 2019 CCC PROBLEM S1'S SOLUTION:

# creating the initial grid.
grid = [

    [1, 2],
    [3, 4]
]

# creating a function to flip horizontally.
def flip_horizontally(grid):

    # swapping the elements in the 2-D array.
    # creating a temp variable to store the value of grid[0]
    temp = grid[0]
    grid[0] = grid[1]
    grid[1] = temp

    pass

# creating a function to flip vertically.
def flip_vertically(grid):

    # creating two temp variables to flip the columns.
    temp1 = [grid[0][1], grid[0][0]]
    temp2 = [grid[1][1], grid[1][0]]

    # swapping.
    grid[1] = temp2
    grid[0] = temp1

    pass

# receiving input from user on what swaps to perform.
string = input()

# creating a for-loop to iterate for the swaps.
for i in range(len(string)):

    # performing a vertical flip if 'V' is specified.
    if string[i] == "V":
        flip_vertically(grid)
    
    # performing a horizontal flip if 'H' is specified.
    else:
        flip_horizontally(grid)

# printing the new flipped grid.
for i in grid:
    for j in i:
        print(j, end = " ")

    print(" ")