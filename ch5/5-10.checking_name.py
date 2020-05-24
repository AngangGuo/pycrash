current_users = ["andrew", "john", "peter", "admin", "ace"]
new_users = ["andrew", "will", "lucy", "Peter"]

lower_users = []
for orig in current_users:
    lower_users.append(orig.lower())

for user in new_users:
    if user.lower() in lower_users:
        print(f"{user} has been used, please select another name.")
    else:
        print(f"{user} is available.")
