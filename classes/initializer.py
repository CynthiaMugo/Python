#initializer: constructor
# Special method in a class
# initializer : method is called whenever the blueprint is used
# to create an object

# me thod function is inside a class
# method you create has to have the self keyword

class Human():
    # self references the object inside the class
    def __init__(self, gender, name):
        print("The initializer was called")
        # print(gender)
        # print(name)
        self.gender = gender
        self.name = name
        if self.gender == "Male":
            self.ribs = 24
            self.curse = "Suffer"
        else :
            self.ribs = 23
            self.curse = "Pain"

    def print_self(self):
        print("------------------------")
        print("name", self.name)
        print("gender", self.gender)
        print("ribs", self.ribs)
        print("curse", self.curse)
        print("--------------------")


# __init__ is called automatically but any other methods inside the class you have to call them yourself
adam = Human(name="Adam", gender="Male") # object from a class
adam.print_self()

eve=Human(name="eve",gender="Female")
eve.print_self()

# eve = Human(name="Eve", gender="female")
# print("name", eve.name)
# print("gender", eve.gender)
# print("ribs", eve.ribs)
# print("curse", eve.curse)