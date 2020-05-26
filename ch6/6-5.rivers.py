rivers = {
    "Brizil": "Cana Brava River",
    "Israel": "Lakhish River",
    "Canada": "Peace River",
    "China": "Yellow River",
    "Vietnam": "Ma River",
}

for country, river in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nCountries:")
for country in rivers.keys():
    print(f"{country}")

print("\nRivers:")
for river in rivers.values():
    print(f"{river}")
