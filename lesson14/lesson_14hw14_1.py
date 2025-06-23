"""
Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи
більше 10-ти студентів, було порушено виняток користувача.

Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
І обробити його поза межами класу.
Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента
"""
class TooManyStudents(Exception):
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name

    def __str__(self):
        return f"{self.error_message} (Group: {self.group_name})"

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender}, {self.age}, {self.first_name}, {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, {self.record_book}"

class Group:

    def __init__(self, number, student_limit=10):
        self.number = number
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group) == self.student_limit:
            raise TooManyStudents("Group limit reached", self.number)
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students} '

test_data = [('Male', 30, 'Steve', 'Jobs', 'AN142'),
('Female', 25, 'Liza', 'Taylor', 'AN145'),
('Male', 26, 'Steve', 'Bobs', 'AN146'),
('Female', 27, 'Liza', 'Taylor', 'AN147'),
('Male', 28, 'Steve', 'Cobs', 'AN148'),
('Female', 25, 'Liza', 'Taylor', 'AN149'),
('Male', 26, 'Steve', 'Dobs', 'AN150'),
('Female', 27, 'Liza', 'Taylor', 'AN151'),
('Male', 28, 'Steve', 'Fobs', 'AN152'),
('Female', 29, 'Liza', 'Taylor', 'AN153'),
('Male', 25, 'Steve', 'Gobs', 'AN154')]

students = [Student(*data) for data in test_data]

gr = Group('PD1')

for student in students:
    try:
        gr.add_student(student)
    except TooManyStudents as e:
        print(f"{student.first_name} {student.last_name} is odd one out" )

# print(gr)
assert str(gr.find_student('Jobs')) == str(students[0]), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
# print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!