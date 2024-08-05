# Raskite visus skaičius iš 1-1000, kuriuose yra 9.

numbers = [num for num in range(1, 1001) if '9' in str(num)]
print(f"Skaiciai nuo 1 iki 1000, kuriuose yra skaitmuo 9: {numbers}")
