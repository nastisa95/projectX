# Leiskite naudotojui įvesti du skaičius. Išspausdinkite, kuris iš jų didesnis už kitą,arba ar jie lygūs.

a = int(input("Iveskite pirma skaiciu: "))
b = int(input("Iveskite antra skaiciu: "))

#print(f"Skaicius {a} didesnis") if a > b else print(f"Skaicius {b} didesnis") if a < b else print(f"skaiciai {a} ir {b} yra lygus")

if a > b:
    print(f"Skaicius {a} didesnis")
elif a < b:
    print(f"Skaicius {b} didesnis")
else:
    print(f"Skaiciai {a} ir {b} yra lygus")
