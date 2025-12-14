def shipping_label(*name, **address):
    for x in name:
        print(x, end=" ")
    print()
    for value in address.values():
        print(value, end=" ")

shipping_label("Dr.", "Spongebob", "Squarepants", "III", street="123 Fake Street")