# Sukurkite skaičių nuo 1 iki 10 spėjimo žaidimą su atsitiktinių skaičių biblioteka. 

import random

generate = random.randint(1, 10)
print("Atspėkite skaičių nuo 1 iki 10.")
lifes = 3

while True:
    print(f"Gyvibiu skaicius {lifes}")
    if lifes == 0:
        print("LOOSER")
        break
    
    guess = input("Įveskite savo spėjimą: ")    
    if guess.isdigit():
        guess = int(guess)
        if guess < 1 or guess > 10:
            print("Įveskite skaičių nuo 1 iki 10.")
        elif guess < generate:
            print("Per mažas skaičius! Bandykite dar kartą.")
            lifes -=1
        elif guess > generate:
            print("Per didelis skaičius! Bandykite dar kartą.")
            lifes -=1
        else:  
            print(f"Teisingai! Skaičius buvo {generate}.")
            break
    else:
        print("Reikia suvest SKAIČIŲ!")

