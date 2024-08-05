# Parašykite nedidelę skaičiuotuvo programą, kuri leistų naudotojui įvesti du skaičius ir simbolį, 
# ir tada atlikti operaciją bei išspausdinti atsakymą.

a = int(input("Iveskite pirma skaiciu: "))
what = input("Iveskite aritmetini zenkla (+ - / *): ")
b = int(input("Iveskite antra skaiciu: "))

if what == "+":
    print(f"{a} + {b} = {a+b}")
elif what == "*":
    print(f"{a} * {b} = {a*b}")
elif what == "/":
    if b != 0:
        print(f"{a} / {b} = {a/b}")
    else:
        print("Is nulio dalinti negalima!")
elif what == "-":
    print(f"{a} - {b} = {a-b}")
else:
    print("Su siuo zenklu negalima atlikti aritmetiniu skaiciavimu!")