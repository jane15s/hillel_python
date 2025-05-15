"""
Програма має виконувати прості математичні дії (+, -, *, /).
Користувачеві пропонується по черзі ввести числа та дію над цими числами,
а програма, виходячи з дії, обчислює та друкує результат.

Зробити перевірку на те, що при діленні дільник не дорівнює 0!
"""

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
user_operator = input("Enter the operator +,-,* or /: ")

# if user_operator == "+":
#     result = first_number + second_number
#     print(result)
# elif user_operator == "-":
#     result = first_number - second_number
#     print(result)
# elif user_operator == "*":
#     result = first_number * second_number
#     print(result)
# elif user_operator == "/":
#     if second_number != 0:
#         result = first_number / second_number
#         print(result)
#     else:
#         print("Number cannot be divided by 0")
# else:
#     print("Invalid operator. Please try again using +,-,* or /")

# using ternary operator for "/" & not zero clause

# elif user_operator == "/":
#     result = first_number / second_number if second_number != 0 else print("Number cannot be divided by 0") # when 0 inserted None goes after print - not valid solution
#     print(result)


match user_operator:
    case "+":
        result = first_number + second_number
        print(result)
    case "-":
        result = first_number - second_number
        print(result)
    case "*":
        result = first_number * second_number
        print(result)
    case "/":
        if second_number != 0:
            result = first_number / second_number
            print(result)
        else:
            print("Number cannot be divided by 0")
    case _:
        print("Invalid operator. Please try again using +,-,* or /")