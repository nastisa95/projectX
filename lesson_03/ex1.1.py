# Leiskite naudotojui įvesti vardą, pavardę ir amžių. 
# Išspausdinkite, ar naudotojas gali patekti į internetinį kazino, ar ne. 21 metai yra amžiaus riba.

name = input('Iveskite savo varda: ')
surname = input('Iveskite savo pavarde: ')
age = int(input('Iveskite savo amziu: '))

if age < 21:
    print(f"Gerb. {name} {surname}, esate per jaunas kazino zaidimams.")
else:
    print(f"Sveikiname prisijungus prie musu online kazino, pone {name} {surname}!")