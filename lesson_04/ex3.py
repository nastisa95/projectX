# Sukurkite mini python programą, kuri kaip įvestį paimtų 
# du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.

def skaiciai(num_1: int, num_2: int) -> list[float]:
    return {
        f"Suma lygi {num_1 + num_2}",
        f"Sandauga lygi {num_1 * num_2}",
        f"Skirtumas lygus {num_1 - num_2}",
        f"Dalmuo lygus {num_1 / num_2}" 
    }

num_1 = int(input("Iveskite pirma skaiciu :"))
num_2 = int(input("Iveskite antra skaiciu :"))

print(skaiciai(num_1, num_2))


# num_1 = int(input("Iveskite pirma skaiciu :"))
# num_2 = int(input("Iveskite antra skaiciu :"))

# print(f"Skaiciu {num_1} ir {num_2} suma lygi {num_1+num_2}")
# print(f"Skaiciu {num_1} ir {num_2} sandauga lygi {num_1*num_2}")
# print(f"Skaiciu {num_1} ir {num_2} skirtumas lygus {num_1-num_2}")
# print(f"Skaiciu {num_1} ir {num_2} dalmuo lygus {num_1/num_2}")
