
fruits = {
    "alma": 1.5,
    "banan": 0.9,
    "portağal": 1.2,
    "armud": 2.0
}

price_deleted = fruits.pop("alma")
print(f"Price Deleted {price_deleted}")


last_element = fruits.popitem()
print(f"Deleted Last Element: {last_element}")


del fruits["banan"]

print("Updated dictionary:", fruits)
