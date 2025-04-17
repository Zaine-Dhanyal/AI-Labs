class Student:
    def __init__(self, rollno, name,age):
        self.rollno = rollno
        self.name = name
        self.age =age
    def display(self):
        print(f'Student Roll No: {self.rollno}, Name: {self.name}, age: {self.age}')
#creating the objects
student1 = Student(1, "Zainab", 20)
student2 = Student(3, "Samreen", 20)
student3 = Student(5, "Dua", 19)
#accessing the attributes
print(student1.name)
print(student2.age)
print(student3.rollno)
#assigning new values
student1.name = "Maryum"
student2.age =23
student3.rollno =7
student1.display()
student2.display()
student3.display()
