# Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.

num_list = []
i = 0
print("Iveskite 10 sveiku skaiciu: ")
while i < 10:
  num_list.append(int(input()))
  i += 1   

print(f"Jus ivedete skaicius: {num_list}")
num_sum = sum(num_list)
print(f"Siu skaiciu suma lygi: {num_sum}")
print(f"Siu skaiciu vidurkis yra: {num_sum/i}")