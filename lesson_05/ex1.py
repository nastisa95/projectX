# Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.

def range_items(numbers: list) -> list[int]:
    return [nr for nr in numbers if not nr % 6]

numberange = list(range(1, 1001))

print(range_items(numberange))
