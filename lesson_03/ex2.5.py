# Sukurkite programą, kuri leistų naudotojui įvesti skaičių seriją ir apskaičiuotų visų skaičių vidurkį. 
# Programa taip pat turėtų išspausdinti visų skaičių list'a ir vidurkį.

num_list = []
print("Iveskite sveiku skaiciu seka. Noredami pabaigti irasykite STOP")
while True:
    user_in = input()
    if user_in == "STOP":
        break
    else:
        num_list.append(float(user_in))

print(f"Jūs įvedėte skaičius: {num_list}")
num_sum = sum(num_list)
kiek = len(num_list)
average = num_sum / kiek
print(f"Siu skaiciu suma lygi: {num_sum}")
print(f"Siu skaiciu vidurkis yra: {average}")