dog = {
    "kind": "Mammals",
    "owner": "Andrew",
}
shorebird = {
    "kind": "Bird",
    "owner": "Millisa",
}
sea_star = {
    "kind": "Echiniderms",
    "owner": "Kevin",
}

pets = [dog, shorebird, sea_star]
for pet in pets:
    print(f"{pet['owner']} has a {pet['kind']}.")
