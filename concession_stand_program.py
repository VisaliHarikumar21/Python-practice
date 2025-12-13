menu = {
    "Popcorn": 6.50,
    "Nachos": 3.25,
    "Hot Dog": 4.30,
    "Pretzel": 2.40,
    "Chips": 3,
    "Burger": 10.9
}
orders = []
total = 0

print("------------------------------------------------------------")
print("                            MENU                            ")
print("------------------------------------------------------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------------------------------------------")

while True:
    order = input("What do you want to order? (Press 'q' to quit)")
    if order.lower() == 'q':
        break
    elif menu.get(order) is not None:
        orders.append(order)
        total += menu.get(order)
    else:
        print(f"{order} not available. Please select from the menu")

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print()
print("Your order:", end=" ")
for order in orders:
    print(order, end=" ")
print()
print(f"You need to pay ${total:.2f}")