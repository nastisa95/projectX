# Parašykite python programą, kuri paprašytų vartotojo įvesti vardą, 
# pavardę, amžių. Įrašykite šias reikšmes į dict duomenų struktūrą ir ją išspausdinkite.

name = input('Iveskite varda: ')
surname = input('Iveskite pavarde: ')
age = input('Iveskite amziu: ')

my_dictionary = {}
my_dictionary["name"] = name
my_dictionary["surname"] = surname
my_dictionary["age"] = age

print(f"Vardas: {my_dictionary['name']}")
print(f"Pavarde: {my_dictionary['surname']}")
print(f"Amzius: {my_dictionary['age']}")