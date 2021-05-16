# 2020 CCC PROBLEM J2'S SOLUTION:

# declaring variable to track time.
time = 0

# receiving the appropriate input's from the user.
P = int(input())
N = int(input())
R = int(input())

# creating variables and tying them to the 'P', 'N', and 'R' values.
total_people = P
people_infected_on_dayZERO = N
people_infected = R

# creating a while-loop to iterate for the period that the people infected are less than the amount we are looking for.
while people_infected <= P:

    # increasing time and performing the necessary arithmetic calculations.
    time += 1
    people_infected += people_infected_on_dayZERO * R
    people_infected_on_dayZERO *= R

# printing the time to the user.
print(time)