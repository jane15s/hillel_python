"""
На вхід функції correct_sentence передається речення. Необхідно повернути його виправлену копію так,
щоб воно завжди починалося з великої літери та закінчувалося крапкою.

Зверніть увагу, що не всі виправлення необхідні.
Якщо речення вже закінчується крапкою, додавати ще одну не потрібно, це буде помилкою.

Вхідні аргументи: string.

Вихідні аргументи: string.

Замість pass необхідно написати Ваше рішення.
"""
import string

def correct_sentence(text: str):
    correct_sent = text[0].upper() + text[1:]
    while correct_sent[-1] in string.punctuation and correct_sent[-1] != ".":
        correct_sent = correct_sent[:-1]
    if not correct_sent.endswith("."):
        correct_sent += "."
    return correct_sent

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

# other_punctuation = string.punctuation.replace(".", "")
# my_example = "some stupid sentence!!"
#
# if not my_example[0].istitle():
#     my_example = my_example.capitalize()
#
# while my_example and my_example[-1] in other_punctuation:
#     my_example = my_example[:-1]
#
# if not my_example.endswith("."):
#     my_example += "."
#
# print(my_example)

# text = "some stupid text"
# correct_sent = text[0].upper() + text[1:]
#
# while correct_sent and correct_sent[-1] in string.punctuation:
#     correct_sent = correct_sent[:-1]
# correct_sent += "."
#
# print(correct_sent)