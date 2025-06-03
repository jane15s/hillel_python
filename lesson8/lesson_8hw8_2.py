"""
Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.

Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без
урахування знаків пунктуації та розмірності букв.

Функція приймає на вхід рядок, та повертає булеве значення True або False

Приклад:

def is_palindrome(text):
    pass
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
"""
import string

def is_palindrome(text):
    new_text =  str()
    for i in text:
        if i not in string.punctuation and i != " ":
            new_text = new_text + i.lower()
    updated_text = new_text[::-1]
    return new_text == updated_text
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

# text = "A man, a plan, a canal: Panama"
# for i in text:
#     if i in string.punctuation:
#         text = text.replace(i, "")
#     if i == " ":
#         text = text.replace(" ", "")
# print(text.lower())
#
#
# if text.lower() == text[::-1]:
#     return True
# else:
#     return False

# text = "A man, a plan, a canal: Panama"
# new_text = str()
# for i in text:
#     if i not in string.punctuation and i != " ":
#         new_text = new_text + i.lower()
#         print(new_text)
# updated_text = new_text[::-1]
# print(updated_text)