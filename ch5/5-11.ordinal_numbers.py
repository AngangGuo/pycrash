numbers = [n for n in range(1, 10)]

postfix = ""
for n in numbers:
    if n == 1:
        postfix = "st"
    elif n == 2:
        postfix = "nd"
    elif n == 3:
        postfix = "rd"
    else:
        postfix = "th"

    print(f"{n}{postfix}")
