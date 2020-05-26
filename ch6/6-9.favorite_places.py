favorite_places = {
    'andrew': ['seattle', 'richmond', 'new westminster', 'surrey'],
    'bob': ['china', 'japan', 'korea'],
    'steve': ['canada', 'england'],
    'joe': ['usa', 'mexico'],
    'kevin': ['vancouver'],
}
count = 0
for n, places in favorite_places.items():
    print(f"{n.title()}'s favorite places are ", end="")
    for place in places:
        if count < (len(places) - 1):
            print(f"{place.title()}, ", end="")
            count = count + 1
        else:
            print(f"and {place.title()}.")
            count = 0

print('----------------------------------')

for name, places in favorite_places.items():
    message = ""
    current = 0
    connector = ""
    # Todo: change are to is if there's one place only
    message = f"{name.title()}'s favorite places are: "

    for place in places:
        current += 1
        if len(places) == current:
            connector = "."
        elif current == len(places) - 1:
            connector = " and "
        else:
            connector = ", "

        # special places
        if place.lower() == 'usa':
            place = place.upper()
        else:
            place = place.title()

        message += f"{place}{connector}"

    print(message)

# Andrew's favorite places are Seattle, Richmond, New Westminster, and Surrey.
# Bob's favorite places are China, Japan, and Korea.
# Steve's favorite places are Canada, and England.
# Joe's favorite places are Usa, and Mexico.
# Kevin's favorite places are and Vancouver.
# ----------------------------------
# Andrew's favorite places are: Seattle, Richmond, New Westminster and Surrey.
# Bob's favorite places are: China, Japan and Korea.
# Steve's favorite places are: Canada and England.
# Joe's favorite places are: USA and Mexico.
# Kevin's favorite places are: Vancouver.
