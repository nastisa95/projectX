# Sukurti programą, leidžiančią vartotojui įvesti pilną sakinį.
# Print the sentence backwards, then all capital letters.
# spausdinti kas antrą sakinio raidę.

text = input('Irasykite savo teksta: ')
print(f"Stai tekstas atbulai: " + text[::-1])
print(f"O cia tekstas didziosiom raidem: " + text.upper())
print(f"Stai kas antra teksto raide: " + text[::2])