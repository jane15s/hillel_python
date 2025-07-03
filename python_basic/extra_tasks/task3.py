"""
Завдання: Парк тварин
Створи два класи:

Animal — описує тварину
Zoo — колекція тварин (звіринець)

Клас Animal:
Повинен мати:
ім’я (name)
вид тварини (species)
вік (age)

Додай метод:

info() — повертає рядок, наприклад:
"Лев на ім’я Сімба, 5 років"

Клас Zoo:
Повинен мати:
список тварин (спочатку порожній)

Методи:
add_animal(animal) — додає тварину до списку
show_all() — виводить інформацію про всіх тварин
get_oldest() — повертає найстарішу тварину
"""

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def info(self):
        return f"{self.species} на ім’я {self.name}, {self.age} років."

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal (self, animal):
        self.animals.append(animal)

    def show_all (self):
        for animal in self.animals:
            print(animal.info())

    def get_oldest (self):
        if not self.animals:
            return None
        oldest = self.animals[0]
        for animal in self.animals[1:]:
            if animal.age > oldest.age:
                oldest = animal
        return oldest

# Приклад використання:

a1 = Animal("Сімба", "Лев", 5)
a2 = Animal("Марті", "Зебра", 7)
a3 = Animal("Глорія", "Бегемот", 4)

zoo = Zoo()
zoo.add_animal(a1)
zoo.add_animal(a2)
zoo.add_animal(a3)

zoo.show_all()

oldest = zoo.get_oldest()
print("Найстаріша тварина:", oldest.info())
"""
Лев на ім’я Сімба, 5 років
Зебра на ім’я Марті, 7 років
Бегемот на ім’я Глорія, 4 років
Найстаріша тварина: Зебра на ім’я Марті, 7 років
"""