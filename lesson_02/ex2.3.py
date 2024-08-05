# Sukurkite programą, kuri iš sakinių, kuriuos jus įvedėt, sukurtų dict, kuriame keys reikštų raides, o values 
# šių raidžių dažnumą tuose sakiniuose. Programa turi reikalauti, kad vartotojas įvestų ne mažiau kaip 3 sakinius.

sent_1 = input('Iveskite 1 sakini: ')
sent_2 = input('Iveskite 2 sakini: ')
sent_3 = input('Iveskite 3 sakini: ')
full_sent = ''.join([sent_1, sent_2, sent_3])
full_sent = full_sent.lower()

lett_list = list(full_sent)
lett_set = set(lett_list)
lett_set = sorted(lett_set)
lett_set.remove(' ')

counts = [lett_list.count(lett) for lett in lett_set]
new_dict = dict(zip(lett_set, counts))

print(new_dict)

# new_dict = {lett: 0 for lett in lett_set}

# for lett in lett_list:
#     new_dict[lett] +=1
