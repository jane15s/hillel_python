"""
Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.

Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім, і другим з кінця.

Приклад:
[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
[1, 1, 2, 1] == [1, 2, 2]
[6, 3, 7] == [6, 7, 3]
"""
import random

random_list = []
for i in range(random.randrange(3,11)):
    random_list.append(random.randint(1,100))
# print(random_list)
new_list = [random_list[0], random_list[2], random_list[-2]]
print(new_list)
