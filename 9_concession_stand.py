# Concession stand program

menu = {"idli": 30.00,
        "dosa": 65.00,
        "pulav": 70.00,
        "pongal": 45.00,
        "poha": 50.00}

cart = []
total = 0

print("-------------- MENU --------------")
for key, value in menu.items():
    print(f"{key:7}: {value:.2f}")
print("----------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------------ YOUR CART ------------")
for food in cart:
    total += menu.get(food)
    print(food)

print()
print(f"Total is: ₹{total:.2f}")