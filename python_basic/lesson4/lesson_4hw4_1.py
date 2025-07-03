"""
Написати програму, яка переміщає всі нулі у кінець списку.
Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
Порядок ненульових чисел має зберегтися!

Приклад:
[0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
[0] -> [0]
[1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
Робити запит на введення даних від користувача не потрібно.
"""

list_one = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
list_two = [0] # -> [0]
list_three = [1, 0, 13, 0, 0, 0, 5] # -> [1, 13, 5, 0, 0, 0, 0]
list_four = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] # -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]


gathered_lists = [list_one, list_two, list_three, list_four]
# for each_list in gathered_lists:
#     updated_list = []
#     for i in each_list:
#         if i != 0:
#             updated_list.append(i)
#     list_of_zeros = []
#     for i in each_list:
#         if i == 0:
#             list_of_zeros.append(i)
#     print(updated_list + list_of_zeros)

for each_list in gathered_lists:
    updated_list = []
    list_of_zeros = []
    for i in each_list:
        if i != 0:
            updated_list.append(i)
        else: list_of_zeros.append(i)
    print(updated_list + list_of_zeros)



