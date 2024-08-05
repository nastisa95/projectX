# Sukurkite duomenų bazę (privilegijuotų naudotojų sąrašas), išspausdinkite konkretų pranešimą 
# su asmeniniu pasveikinimu, jei naudotojas yra privilegijuotas,arba tik "Sveiki atvykę" kitu atveju.

vip = ['monika bellucci', 'antonio banderas', 'leonardo dicaprio', 'timothee chalamet', 'adam sandler', 'jim carrey', 'bruce willis', 'jared leto', 'natalie portman', 'kristen stewart', 'steven spielberg', 'vaidas baumila']
user.lower() = input("Iveskite savo varda: ")

if user in vip:
    print(f"Sveikiname atvykus cia, pone {user}!")
else:
    print("Sveiki atvykę")
