# Practice - Format specifiers
x = 3343.454555
y = 93434.232323
z = -23823.4

# Round to 2 decimal
print(f"x value is {x:.2f}")
print(f"y value is {y:.2f}")
print(f"z value is {z:.2f}")

# Using a thousand separator
print(f"x value is {x:,}")
print(f"y value is {y:,}")
print(f"z value is {z:,}")

# Combination of specifiers
print(f"x value is {x:+,.2f}")
print(f"y value is {y:+,.2f}")
print(f"z value is {z:+,.2f}")