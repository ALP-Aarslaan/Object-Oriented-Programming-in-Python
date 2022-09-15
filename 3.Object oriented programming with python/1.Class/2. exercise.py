class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, Student, ):
        if len(self.students) < self.max_students:
            self.students.append(Student)
        return

    def average_grade(self):
        value = 0
        for student in self.students:
            value = value + Students.get_grade(student)
        return value / len(self.students)


s1 = Students("mohammad", 22, 95)
s2 = Students("Jonayed", 22, 56)
s3 = Students("Sarkar", 22, 89)
s4 = Students("Arslaan", 22, 65)
s5 = Students("Alp", 22, 95)

Cse = Course("Computer Science and Engineering", 10)
Cse.add_students(s1)
Cse.add_students(s2)
Cse.add_students(s3)
Cse.add_students(s4)
Cse.add_students(s5)
print(Cse.average_grade())
print(Cse.name)
