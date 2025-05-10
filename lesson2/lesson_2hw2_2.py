# HW 2.2

user_input = int(input("Enter your 5-digit number: "))
# first_digit = user_input // 10000
# second_digit = user_input % 10000 // 1000
# third_digit = user_input % 1000 // 100
# fourth_digit = user_input % 100 // 10
# fifth_digit = user_input % 10

# using divmod
first_digit, what_left = divmod(user_input, 10000) # first digit = user_input // 10000; what_left = user_input % 10000
second_digit, what_left = divmod(what_left, 1000) # second_digit = what_left // 1000;  what_left = what_left % 1000
third_digit, what_left = divmod(what_left, 100) # third_digit = what_left // 100; what_left = what_left % 100
fourth_digit, fifth_digit = divmod(what_left, 10) # fourth_digit = what_left // 10; fifth_digit = what_left % 10

print(fifth_digit, fourth_digit, third_digit, second_digit, first_digit, sep="")


