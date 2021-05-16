# 2021 CCC PROBLEM J1'S SOLUTION:

# declaring variable to store input from the user regarding the temperature value.
temperature_value = int(input())

# arithmetic calculation to determine the atmospheric pressure.
atmospheric_pressure = (5 * temperature_value) - 400

# printing the atmospheric pressure's value.
print(atmospheric_pressure)

# if-statement for determining the sea level.
if atmospheric_pressure < 100:
    print("1")

elif atmospheric_pressure > 100:
    print("-1")

else:
    print("0")