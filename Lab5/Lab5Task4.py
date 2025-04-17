class Employee:
    def __init__(self,name, salary):
        self.name= name
        self.salary = salary
    def displayDetails(self):
        print(f'Name of Employee: {self.name}, Salary: {self.salary}')
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def displayDetails(self):
        print(f'Name of Employee: {self.name}, Salary: {self.salary}, Department: {self.department}')

class Developer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    def displayDetails(self):
        print(f'Name of Employee: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}')
manager1 = Manager("Zainab", 50000,"HR")
developer1 = Developer("Ayet", 20000,"Python")
employee1 = Employee("Ayet", 20000)
manager1.displayDetails()
developer1.displayDetails()
employee1.displayDetails()
