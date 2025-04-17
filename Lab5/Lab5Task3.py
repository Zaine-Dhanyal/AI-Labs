class Student:
    def __init__(self,rollno, age, grades):
        self.rollno = rollno
        self.age = age
        self.grades = grades
    def averageGrades(self):
        return sum(self.grades)/len(self.grades)
student1= Student(1, 20, [40,50,30,20,10])
print(f'Rollno:{student1.rollno}, Age: {student1.age}, AverageGrades: {student1.averageGrades()}',)
