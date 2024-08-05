# Sukurkite du list'us ir juos sudėkite, įsitikinkite, kad viskas veikia taip, kaip norite.

first_list = [3, 7, 11]
second_list = [2, 6, 12]

total_list = first_list + second_list

sum = 0
for number in total_list:
    sum += number

print(f"Visų elementų sąraše suma: {sum}")