# Sukurkite programą, leidžiančią vartotojui įvesti savo vardą ir amžių.
# Apskaičiuoti metus, kuriais vartotojas gimė.
# Išspausdinti atsakymą į terminalą.

vardas = input("Irasykite varda: ")
amzius = input("Irasykite amziu: ")

gimimo_metai = 2024-int(amzius)

print(f"Labas, {vardas}! Tu gimei {gimimo_metai} metais.")
