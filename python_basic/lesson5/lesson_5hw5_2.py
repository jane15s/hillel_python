"""
Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.
"""
while True:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    user_operator = input("Enter the operator +,-,* or /: ")
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
    ask_to_continue = input("Do you want to continue using this calculater? (type \"yes\" to proceed): ")
    if ask_to_continue != "yes":
        print("ok, maybe next time")
        break
