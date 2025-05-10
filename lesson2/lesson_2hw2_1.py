# HW 2.1

user_input = int(input("Enter your 4-digit number: "))
# first_digit = user_input // 1000
# second_digit = user_input % 1000 // 100
# third_digit = user_input % 100 // 10
# fourth_digit = user_input % 10

# using divmod
first_digit, what_left = divmod(user_input, 1000) # first_digit = user_input // 1000; what_left = user_input % 1000
second_digit, what_left = divmod(what_left, 100) # second_digit = what_left // 100; what_left = what_left % 100
third_digit, fourth_digit = divmod(what_left, 10) # third_digit = what_left // 10, fourth_digit = what_left % 10

print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)


