# Parašykite programą, kuri patikrintų, ar duotas skaičius yra tobulasis kvadratas.

import math

num_input = int(input("Įveskite skaičių: "))

def perfect_square(number: int) -> bool:
    if number < 0:
        return False
    sqrt_num = math.sqrt(number)
    return int(sqrt_num) ** 2 == number

if perfect_square(num_input):
    print(f"{num_input} yra tobulasis kvadratas.")
else:
    print(f"{num_input} nėra tobulasis kvadratas.")
