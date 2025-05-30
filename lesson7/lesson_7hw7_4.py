"""
Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range)
для 100 елементів, за наступними правилом:
Один список з числами кратними 3, інший з кратними числами 5.
За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
Функція повинна повернути цю множину як результат своєї роботи.

def common_elements():
		pass

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

"""

def common_elements():
    first_set = {i for i in range(101) if i % 3 == 0}
    second_set = {i for i in range(101) if i % 5 == 0}
    return first_set.intersection(second_set)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

# lst_for3 = []
# lst_for5 = []
# for i in range(101):
#     if i % 3 == 0:
#         lst_for3.append(i)
#     if i % 5 == 0:
#         lst_for5.append(i)
# first_set = set(lst_for3)
# second_set = set(lst_for5)
# result = first_set.intersection(second_set)
# return result

# lst_for3 = []
# lst_for5 = []
# for i in range(0, 101):
#     if i % 3 == 0:
#         lst_for3.append(i)
#     if i % 5 == 0:
#         lst_for5.append(i)
# first_set = set(lst_for3)
# second_set = set(lst_for5)
# print(first_set)
# print(second_set)
# result = first_set.intersection(second_set)
# print(result)