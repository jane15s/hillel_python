"""
Напиши функцію safe_divide(a, b), яка приймає два числа та повертає результат ділення a / b.
Якщо дільник (b) дорівнює нулю — поверни рядок "Ділення на нуль неможливе".
"""
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Ділення на нуль неможливе"
#
# safe_divide(10, 2) # → 5.0
# safe_divide(5, 0) # → "Ділення на нуль неможливе"
#
# assert safe_divide(6, 2) == 3.0
# assert safe_divide(1, 0) == "Ділення на нуль неможливе"

"""
Напиши програму, яка:

Запитує у користувача два числа (input()).
Пробує їх перетворити в float.
Питає, яку операцію виконати (+, -, *, /).
Виконує операцію та виводить результат.

🔸 Якщо користувач вводить не число — виведи "Ви ввели не число!"
🔸 Якщо при діленні дільник = 0 — виведи "Ділення на нуль!"
🔸 Якщо операція не підтримується — виведи "Невідома операція!"
Додатково: зациклити, поки не буде введено валідних даних.
"""
unfinished = True

while unfinished:
    unfinished = False
    try:
        first_number = float(input("Введіть перше число: "))
        second_number = float(input("Введіть друге число: "))
        user_operator = input("Виберіть операцію (+, -, *, /): ")

        match user_operator:
            case "+":
                result = first_number + second_number
            case "-":
                result = first_number - second_number
            case "*":
                result = first_number * second_number
            case "/":
                result = first_number / second_number
            case _:
                print("Невідома операція!")
                continue

        if not unfinished:
            print("Результат:", result)

    except ValueError:
        print("Ви ввели не число!")
        unfinished = True

    except ZeroDivisionError:
        print("Ділення на нуль!")
        unfinished = True
