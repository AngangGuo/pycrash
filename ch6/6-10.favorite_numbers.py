favorite_numbers = {
    "andrew": [1144, 66],
    "mellisa": [23, 9],
    "kevin": [25000, 37],
    "john": [13, 45, 22],
    "will": [45],
}

for name, nums in favorite_numbers.items():
    msg = f"{name.title()}'s favorite numbers are: "
    current = 0
    for num in nums:
        current += 1
        sep = ", "
        if current == len(nums):
            sep = "."
        msg += str(num) + sep
    print(msg)
