#Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.

def float_list_in() -> list[float]:
    user_input = input("Įveskite skaičius, atskirtus tarpais: ")
    return [float(num) for num in user_input.split()]

print(float_list_in())
