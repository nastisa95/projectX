# Sukurkite studentų vardų ir jų pažymių žodyną:
#    Studentų vardus saugokite kaip raktus, o jų pažymius - kaip reikšmes žodyne.

# Apskaičiuokite visų studentų vidutinį pažymį:
#    Naudokite sum() ir len() funkcijas apskaičiuoti bendrą ir pažymių skaičių, atitinkamai, 
#    o tada bendrąjį skaičių padalinkite iš skaičiaus, kad gautumėte vidurkį.

# Pašalinti studentus, kurių pažymiai mažesni nei 80, iš žodyno:
#    Naudokite set, kad sukurtumėte studentų vardų rinkinį, kurių pažymiai yra mažesni nei 80.

# Pažiūrėti, ar konkretus studentas egzistuoja žodyne:
#    Įveskite studento vardą iš vartotojo.
#    Naudokite in operatorių, norėdami patikrinti, ar studento vardas egzistuoja žodyne.
#    Spausdinkite pranešimą, rodantį, ar studento vardas yra rastas, ar ne.

stud_pas = {
    'Monika Bellucci': 90, 
    'Antonio Banderas': 96, 
    'Leonardo DiCaprio': 88, 
    'Timothee Chalamet': 99, 
    'Adam Sandler': 42, 
    'Jim Carrey': 64,
    'Bruce Willis': 92,
    'Jared Leto': 26,
    'Natalie Portman': 72,
    'Kristen Stewart': 11,
    'Steven Spielberg': 89,
    'Vaidas Baumila': 54
    }

rate_average = sum(stud_pas.values()) / len(stud_pas)
print(f"Visu studentu vidurkis yra: {rate_average}")

badass_list = []
for key, value in stud_pas.items():
    if value < 80:
        badass_list.append(key)
print(f'Prastai mokosi: {badass_list}')

for key in badass_list:
    del stud_pas[key]
print(f'Gerai mokosi: {list(stud_pas.keys())}')

find = input('Irasykite ieskomo studento varda ir pavarde: ')
print(f'Studentas {find} yra sarase: {find in stud_pas}')
