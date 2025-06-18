"""
Створи клас User, який буде описувати користувача.

Вимоги:
Клас повинен мати:

Ім'я (name)

Вік (age)

Електронну пошту (email)

Додай метод greet(), який виводить привітання:
"Привіт, мене звати <name> і мені <age> років."

Створи 2 екземпляри цього класу з різними даними та виклич метод greet() для кожного з них.
"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greed(self):
        print(f"Привіт, мене звати {self.name} і мені {self.age} років.")
    #
    # def __str__(self):
    #     return f"Привіт, мене звати {self.name} і мені {self.age} років."


user1 = User("Vasya", 10)
user2 = User("Katya", 12)
# print(user1)
# print(user2)

user1.greed()
user2.greed()