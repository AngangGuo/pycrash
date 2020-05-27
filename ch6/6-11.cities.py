cities = {
    "vancouver": {
        "country": "canada",
        "population": 2_463_000,
        "fact": "Vancouver has the highest population density in Canada, with over 5,400 people per square kilometre",
    },
    "beijing": {
        "country": "china",
        "population": 21_000_000,
        "kind": " is the capital of the People's Republic of China.",
    },
    "Jerusalem": {
        "country": "israel",
        "population": 919_000,
        "kind": "Jerusalem is a city in the Middle East, located on a plateau in the Judaean Mountains between the "
                "Mediterranean and the Dead Sea.",
    },
}

for city, info in cities.items():
    print(city + ": ")
    for k, v in info.items():
        print(f"\t{k}: {v}")
