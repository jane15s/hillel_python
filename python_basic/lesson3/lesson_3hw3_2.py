"""
Ваша програма має перенести останній елемент списку з кінця на початок,
тобто, останній елемент списку має стати першим.
Послідовність інших елементів не має змінюватися.
Порожній список або список з одним елементом повинен залишитися незмінним.

Кількість елементів у списку може бути будь-яким – нуль та більше!

Приклади:
[12, 3, 4, 10] => [10, 12, 3, 4]
[1] => [1]
[] => []
[12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
Робити запит на введення даних від користувача не потрібно.
"""

list1 = [12, 3, 4, 10] # => [10, 12, 3, 4]
list2 = [1] # => [1]
list3 = []  #=> []
list4 = [12, 3, 4, 10, 8] # => [8, 12, 3, 4, 10]

# if len(list1) > 1:
#     list1.insert(0, list1[-1])
#     list1.pop()
#     print(list1)
# else: print(list1)
#
# if len(list2) > 1:
#     list2.insert(0, list2[-1])
#     list2.pop()
#     print(list2)
# else: print(list2)
#
# if len(list3) > 1:
#     list3.insert(0, list3[-1])
#     list3.pop()
#     print(list3)
# else: print(list3)
#
# if len(list4) > 1:
#     list4.insert(0, list4[-1])
#     list4.pop()
#     print(list4)
# else: print(list4)

#using slicing & concatenation
if len(list1) > 1:
    first_part = list1[-1:]
    second_part = list1[:-1]
    print(first_part + second_part)
else: print(list1)

if len(list2) > 1:
    first_part = list2[-1:]
    second_part = list2[:-1]
    print(first_part + second_part)
else: print(list2)

if len(list3) > 1:
    first_part = list3[-1:]
    second_part = list3[:-1]
    print(first_part + second_part)
else: print(list3)

if len(list4) > 1:
    first_part = list4[-1:]
    second_part = list4[:-1]
    print(first_part + second_part)
else: print(list4)