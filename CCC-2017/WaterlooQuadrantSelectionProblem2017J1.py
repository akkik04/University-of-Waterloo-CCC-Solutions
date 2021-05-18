# 2017 CCC PROBLEM J1'S SOLUTION:

# function receiving two arguments as the x-coordinate and y-coordinate.
def quadrant_selection(x_cor, y_cor):

    # if-statement to determine the quadrant in which the point lies.
    if x_cor > 0 and y_cor > 0:

        return '1'
    
    elif x_cor < 0 and y_cor > 0:

        return '2'
    
    elif x_cor < 0 and y_cor < 0:

        return '3'

    else:
            
        return '4'

# receiving input for the value of the x-coordinate and y-coordinate.
x_cor = int(input())
y_cor = int(input())

# printing out the quadrant that the point is present in.
print(quadrant_selection(x_cor, y_cor))