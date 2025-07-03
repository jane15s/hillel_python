"""
Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.

Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному
(на уроці говорили що треба перевірки й виправити якщо юзер вводить букви в неправильному порядку).

Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв

Приклад:

"a-c" -> abc
"a-a" -> a
"s-H" -> stuvwxyzABCDEFGH
"a-A" -> abcdefghijklmnopqrstuvwxyzA
"""
import string

# print(string.ascii_letters)
allowed_values = string.ascii_letters
users_input = input("Enter two letters to select the range using \"-\" in between, e.g. \"b-s\": ")
users_input = users_input.replace(" ", "")

if len(users_input) != 3:
    print("Wrong input, please follow the rules")
elif users_input[1] != "-":
    print("Wrong or missing delimiter, please use \"-\"")
elif users_input[0] not in allowed_values or users_input[2] not in allowed_values:
    print(f"Check your input again. Please make sure that you've used the following letters: {allowed_values}")
else:
    required_letters = users_input.split("-")
    # print(required_letters)
    first_char = required_letters[0]
    second_char = required_letters[1]

    start_index = allowed_values.find(first_char)
    end_index = allowed_values.find(second_char)
    # print(start_index, end_index)
    if end_index < start_index:
        print("Note: You entered the letters in reverse order. The range will still be generated correctly.")
    min_ind = min(start_index, end_index)
    max_ind = max(start_index, end_index)
    result = allowed_values[min_ind:max_ind + 1]
    print(result)


