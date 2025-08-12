class Shape():
    def __init__(self, name):
        self.name = name

    def describe_shape(self):
        print(f"This shape is called {self.name}")

    def area(self):
        print(f"For shape {self.name} area not implemented")
        return None


class Rectangle(Shape): #super - refers to the class you are inheriting form
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.width = width
        self.length = length
    
    def area(self):
        area = self.width * self.length
        print(f"For {self.name}, area is {area}")
        return area
    
class Circle(Shape): #super - refers to the class you are inheriting form
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        area = 3.142 * self.radius**2
        print(f"For {self.name}, area is {area}")
        return area
    
class Triangle(Shape):
    def __init__(self, length, width, height):
        super().__init__("Triangle")
        self.length = length
        self.width = width
        self.height = height

r1 = Rectangle(10, 3)
r1.describe_shape()
print("The name is", r1.name)
print("The length is", r1.length)
r1.area()

c1 = Circle(7)
c1.describe_shape()
c1.area()

t1 = Triangle(4, 6, 9)
t1.describe_shape()
t1.area()