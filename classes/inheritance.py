class Shape():
    def __init__(self, name):
        self.name = name

    def describe_shape(self):
        print(f"This shape is called {self.name}")


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

r1 = Rectangle(10, 3)
r1.describe_shape()
print("The name is", r1.name)
print("The length is", r1.length)
r1.area()

c1 = Circle(7)
c1.describe_shape()
c1.area()

# run the class before inheritance
# shape1 = Shape(name="Circle") #kwargs
# shape1.describe_shape()

class User():
    def __init__(self, name, email, phone, password, user, discount=0):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.discount = discount
        self.user = user
        self.is_locked = False

    def say_my_name(self):
        print(f"My name is {self.name}")

    def print_details(self):
        print("--------------------------")
        print("User:", self.user)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("Discount:", self.discount)
        print("--------------------------")

    def login(self):
        if self.is_locked:
            print("Account already locked")
            return
        
        for i in range(1, 4):
            password = input(f"Enter your password Attempt {i}: ")
            if self.password == password:
                print("Log in success")
                return
        self.is_locked = True
        print("Account locked! Contact admin")

class Employee(User):
    def __init__(self, name, email, phone, password, salary):
        super().__init__(name, email, phone, password, "employee", 10) #*args
        self.salary = salary

class Customer(User):
    def __init__(self, name, email, phone, password):
        super().__init__(name, email, phone, password, "customer", 0)

emp1 = Employee(name="Cynthia", email="cynthia@cy.com", phone=789765497, password="password", salary=40000)
emp1.print_details()

c1 = Customer(name="Viola", email="viola@viola.com", phone=722478098, password="password")
c1.print_details()

emp1.login()