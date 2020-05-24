fav_food = "beef"
print("Is beef your favourite food? I think so.")
print(fav_food == "beef")
print("Is apple your favourite food? I don't think so.")
print(fav_food == "apple")

print("-----------------------")

file_name = "names.xls"
excel_ext = "xls"
word_ext = ".doc"
print("Is this Excel file? I predict True.")
print(file_name[-3] == excel_ext)
print("Is this a Word file? I predict False.")
print(file_name[-3] == word_ext)

print("-----------------------")

my_age = 40
your_age = 20
print("Am I older than you? I predict True")
print(my_age > your_age)
print("Am I younger than you? I predict False")
print(my_age < your_age)

print("-----------------------")

name = "Andrew"
print("Is the lower case of you name andrew? I predict True.")
print(name.lower() == "andrew")
print("Is the lower case of you name peter? I predict False.")
print(name.lower() == "peter")

print("-----------------------")

num1 = 3
num2 = 100
num3 = 44
num4 = 234
print(f"Does the num3({num3}) in between of num1({num1}) and num2({num2})? I predict True.")
print(num1 < num3 < num2)
print(f"Does the num3({num3}) out of num1({num1}) and num2({num2})? I predict False.")
print(num1 >= num3 >= num2)
print(f"Does the num4({num4}) out of num1({num1}) and num2({num2})? I predict True.")
print(num4 < num1 or num4 > num2)
print(f"Does the num4({num4}) in between num1({num1}) and num2({num2})? I predict False.")
print(num1 < num4 < num2)

print("-----------------------")

list = [1, 3, 5, 7, 9]
num5 = 4
num6 = 7
print(f"Is num5({num5}) in the list({list})? I predict False.")
print(num5 in list)
print(f"Is num6({num6}) in the list({list})? I predict True.")
print(num6 in list)
