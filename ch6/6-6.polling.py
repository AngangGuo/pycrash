favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

person = ['jen', 'andrew', 'edward', 'john']

for name in favorite_languages.keys():
    if name in person:
        print(f"{name.title()}, thanks for your response.")
    else:
        print(f"{name.title()}, please take a poll.")
