class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
            return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
class Triangle(Shape):
    def __init__(self, base, height):
        self.base= base
        self.height= height
    def area(self):
        return 0.5*self.base*self.height
shapes=[
Circle(4),
Rectangle(5,6),
Triangle(3,7)
]
for shape in shapes:
    print(shape.area())
