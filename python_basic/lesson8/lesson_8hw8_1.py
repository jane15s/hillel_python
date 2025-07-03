"""
Ваше завдання — написати функцію add_one, яка приймає список із цифр, які у свою чергу є одним числом.
До нього необхідно додати 1.

Тобто. Вам необхідно з набору цифр, що входять до списку, отримати число, скласти його з 1 і отриману суму,
знову розбити на список із цифр.

В результаті функція повертає список із цифр, що становлять значення суми.

Так зі списку з цифрами [1, 2, 3, 4], має вийти число 1234. До нього додаємо 1, і отримуємо 1235.
Після цього потрібно розбити отримане число на складові цифри.
У результаті має бути список [1, 2, 3, 5], який повертає функція.

Якщо ви хочете себе перевірити, використайте цей unit test

def add_one(some_list):
    pass
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
"""

def add_one(some_list):
    number = int("".join(map(str, some_list))) +1
    return [int(i) for i in str(number)]
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1' 
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2' 
assert add_one([0]) == [1], 'Test3' 
assert add_one([9]) == [1, 0], 'Test4' 
print("ОК")

# some_list = [1, 2, 3, 4]
# number = int("".join(map(str, some_list))) +1

# converted_list = str(some_list)
# edited_string = converted_list.replace(", ", "")
# edited_string2 = edited_string.replace("[", "")
# edited_string3 = edited_string2.replace("]", "")
# number = int(edited_string3) + 1
# print(number)