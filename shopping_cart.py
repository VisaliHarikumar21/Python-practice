# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    foods.append(food)
    price = float(input(f"Enter the price of {food}: Rs."))
    prices.append(price)

print("---------- YOUR CART -------------")
for food in foods:
    print(food, end= " ")
print()
for price in prices:
    total += price

print(f"Your total in cart: {total:,.2f}")