glossaries = {
    "list": "[1, 2, 3]",
    "dictionary": '{"Name": "Andrew"}',
    "const": "PI = 3.14159",
    "variable": "name = 'Andrew'",
    "for": "for name, age in students.items():",
}

for item, desc in glossaries.items():
    print(f"{item.title()}: {desc}")
