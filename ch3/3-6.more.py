guests = ["Mark", "Kevin", "Mellisa"]
msg = "I'd like to invite you to have a dinner with us on 5/18. Thanks, Andrew"

print("\nHi friends, I found a large table today. I'll invite more friends come to enjoy the dinner with us!\n")

guests.insert(0, "Noor")
guests.append("Jocelyn")
guests.insert(3, "Lisa")

print(f"Hi {guests[0]}, {msg}")
print(f"Hi {guests[1]}, {msg}")
print(f"Hi {guests[2]}, {msg}")
print(f"Hi {guests[3]}, {msg}")
print(f"Hi {guests[4]}, {msg}")
print(f"Hi {guests[5]}, {msg}")