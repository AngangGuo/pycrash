guests = ["Mark", "Kevin", "Mellisa"]
msg = "I'd like to invite you to have a dinner with us on 5/18. Thanks, Andrew"

print("\nHi friends, I found a large table today. I'll invite more friends come to enjoy the dinner with us!\n")

guests.insert(0, "Noor")
guests.insert(3, "Lisa")
guests.append("Jocelyn")

print("\nSorry, I haven't received the new table yet. I can invite only two person for dinner.\n")

sorry = "Sorry, I can't invite you for dinner. See you next time."
guest = guests.pop()
print(f"Hi {guest}, {sorry}")
guest = guests.pop()
print(f"Hi {guest}, {sorry}")
guest = guests.pop()
print(f"Hi {guest}, {sorry}")
guest = guests.pop()
print(f"Hi {guest}, {sorry}")

print(f"Hi {guests[0]}, {msg}")
print(f"Hi {guests[1]}, {msg}")

# Delete from the last one to first one
# Or delete the first one repeatedly
del guests[1]
del guests[0]
print(guests)

if guests:
    print("not empty")
else:
    print("empty")

