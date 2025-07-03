"""
Вам необхідно написати функцію find_unique_value, яка приймає список із чисел,
знаходить серед них унікальне число та повертати його.
Унікальне число - це число, яке зустрічається в списку один раз.
Випадок, коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.

Приклад:

def find_unique_value(some_list):
   pass
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
"""

def find_unique_value(some_list):
    for i in some_list:
        if some_list.count(i) == 1:
            return i
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

# print(find_unique_value([1, 2, 1, 1])) # == 2, 'Test1'
# print(find_unique_value([2, 3, 3, 3, 5, 5])) # == 2, 'Test2'
# print(find_unique_value([5, 5, 5, 2, 2, 0.5])) # == 0.5, 'Test3'

# some_list = [5, 5, 5, 2, 2, 0.5]
# unique_value = []
# for i in some_list:
#     if some_list.count(i) == 1:
#         unique_value.append(i)
# print(float(unique_value[0]))


# list_to_set = set(some_list)
# set_to_list = list(list_to_set)
# print(set_to_list)