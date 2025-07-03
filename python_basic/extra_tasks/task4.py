"""
Завдання: Автопарк
Створи два класи:
1. Car — описує автомобіль
2. Garage — колекція автомобілів

Клас Car повинен мати:
brand — марка машини (наприклад, "Toyota")
model — модель (наприклад, "Corolla")
year — рік випуску

Метод:
info() — повертає рядок типу:
Toyota Corolla, 2015 рік

Клас Garage повинен мати:
список машин (початково порожній)

Методи:

add_car(car) — додає машину до гаража
show_all() — виводить всі машини
get_oldest() — повертає найстарішу машину
get_newest() — повертає найновішу машину
"""
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"{self.brand} {self.model}, {self.year} рік"

class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_all (self):
        for car in self.cars:
            print(car.info())

    def get_oldest(self):
        if not self.cars:
            return None
        oldest = self.cars[0]
        for car in self.cars:
            if car.year < oldest.year:
                oldest = car
        return oldest

    def get_newest(self):
        if not self.cars:
            return None
        newest = self.cars[0]
        for car in self.cars:
            if car.year > newest.year:
                newest = car
        return newest


c1 = Car("Toyota", "Corolla", 2015)
c2 = Car("Tesla", "Model S", 2020)
c3 = Car("BMW", "X5", 2012)

garage = Garage()
garage.add_car(c1)
garage.add_car(c2)
garage.add_car(c3)

garage.show_all()
print("Найстаріша машина:", garage.get_oldest().info())
print("Найновіша машина:", garage.get_newest().info())
"""
Очікуваний результат:

Toyota Corolla, 2015 рік
Tesla Model S, 2020 рік
BMW X5, 2012 рік
Найстаріша машина: BMW X5, 2012 рік
Найновіша машина: Tesla Model S, 2020 рік
"""

# додаткова вправа на розуміння важливості перевірки списку на порожність
def max_in_list(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for i in numbers[1:]:
        if i > max_num:
            max_num = i
    return max_num

assert max_in_list([3, 5, 2, 9, 1]) == 9
assert max_in_list([-10, -5, -1]) == -1
assert max_in_list([0]) == 0
assert max_in_list([]) is None