guests = ["Mark", "Kevin", "Mellisa"]
msg = "I'd like to invite you to have a dinner with us on 5/18. Thanks, Andrew"
print(f"Hi {guests[0]}, {msg}")
print(f"Hi {guests[1]}, {msg}")
print(f"Hi {guests[2]}, {msg}")

print(f"\nSorry, {guests[1]} can't make it.\n")

guests[1] = "Ace"
print(f"Hi {guests[0]}, {msg}")
print(f"Hi {guests[1]}, {msg}")
print(f"Hi {guests[2]}, {msg}")
