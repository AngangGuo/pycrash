colors = ["red“，”blue"]
del colors[0]

# del colors[1]
# Traceback (most recent call last):
#   File "3-11.index_error.py", line 4, in <module>
#     del colors[1]
# IndexError: list assignment index out of range

# fix: only 1 item left
del colors[0]
