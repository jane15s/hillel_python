"""
Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
Тобто, в результаті повинен вийти список із 2-х списків.
Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.

Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
у списку парна кількість елементів і в списку непарна кількість елементів.

Приклади:
Було => стало
[1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
[1, 2, 3] => [[1, 2], [3]]
[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
[1] => [[1], []]
[] => [[], []]
Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
Робити запит на введення даних від користувача не потрібно.
"""

first_list = [1, 2, 3, 4, 5, 6] # => [[1, 2, 3], [4, 5, 6]]
second_list = [1, 2, 3] # => [[1, 2], [3]]
third_list = [1, 2, 3, 4, 5] # => [[1, 2, 3], [4, 5]]
fourth_list = [1] # => [[1], []]
fifth_list = [] # => [[], []]

# mid_index = len(first_list) // 2
# if len(first_list) % 2 != 0: # if smth left - odd, if not - even
#     mid_index +=1 # mid_index = mid_index + 1
# first_list1 = first_list[:mid_index] # elements of list before mid_index value
# first_list2 = first_list[mid_index:] # elements of list after mid_index value
# final_list1 = [first_list1, first_list2]
# print(final_list1)

mid_index = len(first_list) // 2
if len(first_list) % 2 != 0:
    mid_index +=1
final_list1 = [first_list[:mid_index], first_list[mid_index:]]
print(final_list1)

mid_index = len(second_list) // 2
if len(second_list) % 2 != 0:
    mid_index +=1
final_list2 = [second_list[:mid_index], second_list[mid_index:]]
print(final_list2)

mid_index = len(third_list) // 2
if len(third_list) % 2 != 0:
    mid_index +=1
final_list3 = [third_list[:mid_index], third_list[mid_index:]]
print(final_list3)

mid_index = len(fourth_list) // 2
if len(fourth_list) % 2 != 0:
    mid_index +=1
final_list4 = [fourth_list[:mid_index], fourth_list[mid_index:]]
print(final_list4)

mid_index = len(fifth_list) // 2
if len(fifth_list) % 2 != 0:
    mid_index +=1
final_list5 = [fifth_list[:mid_index], fifth_list[mid_index:]]
print(final_list5)

#using loop (practicing lesson4)
all_lists = [first_list, second_list, third_list, fourth_list, fifth_list]

for single_list in all_lists:
    mid_index = len(single_list) // 2
    if len(single_list) % 2 != 0:
        mid_index += 1
    final_list = [single_list[:mid_index], single_list[mid_index:]]
    print(final_list)
