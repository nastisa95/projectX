# Create program that allows user to enter text
# Convert that text to Leet speak 1337
# Print outcome

text = input('Irasykite savo teksta: ')

# print(text.replace('a', '4'; 'A', '4'))

my_dictionary = {'A': '4', 'a': '4', 'E': '3', 'e': '3', 'I': '1', 'i': '1', 'O': '0', 'o': '0', 'S': '5', 's': '5', 'T': '7', 't': '7'}
for key, value in my_dictionary.items():
    print(text.replace(key, value))
