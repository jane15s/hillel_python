from student import Student
from group import Group
from exception import TooManyStudents


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 26, 'Anna', 'Taylor', 'AN146')
st4 = Student('Female', 27, 'Zulfiia', 'Taylor', 'AN147')
gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)

except TooManyStudents as error:
    print(error)
except Exception as error:
    print(error)

assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
assert st1.compare(st1)
# assert st1.compare(st2)