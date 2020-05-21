foods = ("Steamed Farm Vegetable Medley",
         "Truffles Caesar",
         "Lemon Blueberry Cheese Cake",
         "Whole Roasted Striploin",
         "Fresh prawns sautéed to order with garlic, chili, cilantro and lemon")
print("Buffet menu:")
print("============")
for food in foods:
    print(food)

# foods[0]="Nothing"
# Traceback (most recent call last):
#   File "4-13.buffet.py", line 9, in <module>
#     foods[0]="Nothing"
# TypeError: 'tuple' object does not support item assignment

print()
print("Changed menu:")
print("=============")
foods = ("Steamed Farm Vegetable Medley",
         "Truffles Caesar",
         "Dark Chocolate Mousse",
         "Whole Roasted Striploin",
         "B.C. Smoked Salmon Caper Linguini")
for food in foods:
    print(food)
