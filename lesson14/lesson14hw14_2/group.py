from student import Student
from exception import TooManyStudents

class Group:

    def __init__(self, number, student_limit=10): # перевірено на ліміті 3
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