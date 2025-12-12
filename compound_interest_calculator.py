# Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be in negative or zero. Enter again!")

while rate <= 0:
    rate = float(input("Enter the interest rate (in %): "))
    if rate <= 0:
        print("Rate can't be in negative or zero. Enter again!")

while time <= 0:
    time = float(input("Enter the tenure (in years): "))
    if time <= 0:
        print("Tenure can't be in negative or zero. Enter again!")

print(principle)
print(rate)
print(time)

compound_interest = principle * pow((1 + rate/100), time)
print(f"Compound interest is {compound_interest:,.2f}")