"""
Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.

Змінна не може:

починатися з цифри
містити великі літери,
пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
бути жодним із зареєстрованих слів.
При цьому повне ім'я змінної повинно складатись не більш чим з одного нижнього підкреслення "_".

Список зареєстрованих слів можна взяти із keyword.kwlist.

У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))

_ => True
__ => False
___ => False
x => True
get_value => True
get value => False
get!value => False
some_super_puper_value => True
Get_value => False
get_Value => False
getValue => False
3m => False
m3 => True
assert => False
assert_exception => True
"""
import keyword
import string

# while True:
#     user_input = input("Enter a valid variable name: ")
#     underscore_excluded = string.punctuation.replace("_", "")
#     if user_input == "_":
#         print(user_input + " => True")
#     elif not user_input[0].isdigit() and user_input.islower() and not any(char.isspace() for char in user_input) and not any(char in underscore_excluded for char in user_input) and user_input not in keyword.kwlist:
#         print(user_input + " => True")
#     else:
#         print(user_input + " => False")
#         # break


test_data = [
    "_",
    "__",
    "___",
    "x",
    "get_value",
    "get value",
    "get!value",
    "some_super_puper_value",
    "Get_value",
    "get_Value",
    "getValue",
    "3m",
    "m3",
    "assert",
    "assert_exception"
]
underscore_excluded = string.punctuation.replace("_", "")
for test_value in test_data:
    if test_value in keyword.kwlist: # not keyword
        print(f"{test_value} => False")
        continue
    if len(test_value) > 0 and test_value[0].isdigit(): # not "" and ind 0 char is not digit
        print(f"{test_value} => False")
        continue
    if any(char.isupper() for char in test_value): # no upper-case letters
        print(f"{test_value} => False")
        continue
    if any(char in underscore_excluded for char in test_value): # no punctuation marks except "_"
        print(f"{test_value} => False")
        continue
    if test_value.count("_") > 1 and "__" in test_value: # only one underscore for single-digit value & snake case in general
        print(f"{test_value} => False")
        continue
    if any(char.isspace() for char in test_value): # no spaces
        print(f"{test_value} => False")
        continue
    print(f"{test_value} => True")





