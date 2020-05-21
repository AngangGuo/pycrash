pizzas = ["Hawaiian", "BBQ Chicken", "Cheese Lovers"]
friend_pizzas=pizzas[:]
pizzas.append("Marinara")
friend_pizzas.append("Tomato sauce")
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(f"\t- {pizza}")
print()
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t- {pizza}")

