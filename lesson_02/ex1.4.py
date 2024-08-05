# Parašykite python programą, kuri sujungia visas list esančias string 
# duomenų tipo reikšmes (visi elementai yra string tipo, list'a sukurkite patys)

text_list = ["Virė", "mama", "košę", "makalošę"]

long_string = ''
for word in text_list:
    long_string += word

text_list = [long_string]

print(text_list)


# or

text_2 = ", ".join(text_list)
print(text_2)