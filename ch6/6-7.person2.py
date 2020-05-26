andrew = {
    "first_name": "andrew",
    "last_name": "guo",
    "age": 88,
    "city": "vancouver",
}

kevin = {
    "first_name": "kevin",
    "last_name": "guo",
    "age": 18,
    "city": "toronto",
}

mellisa = {
    "first_name": "mellisa",
    "last_name": "lu",
    "age": 38,
    "city": "taiwan",
}

people = [andrew, kevin, mellisa]
for name in people:
    # for k, v in info.items():
    print(f"{name['first_name'].title()} {name['last_name'].title()} is {name['age']} years old.")
    print(f"{name['first_name'].title()} {name['last_name'].title()} lives in {name['city'].title()}.")

