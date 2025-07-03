"""
Ваше завдання — написати програму, яка перемножує всі цифри,
введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
Користувач вводить число з клавіатури.

Приклади:

999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
1000 -> 0
423 -> 8
33 -> 9
25 -> 0
1 -> 1
"""

user_input = input("Enter a number: ")
user_input = user_input.replace(" ", "")
if not user_input.isdigit():
    print("Please enter the number, no letters or symbols allowed")
else:
    required_value = int(user_input)
    while required_value > 9:
        result = 1
        for digit in str(required_value):
            result = result * int(digit)
        required_value = result

    print(required_value)
