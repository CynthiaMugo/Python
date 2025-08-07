#initializer: constructor
# Special method in a class
# initializer : method is called whenever the blueprint is used
# to create an object

# me thod function is inside a class
# method you create has to have the self keyword

class Human():
    def __init__(self):
        print("The initializer was called")
    def another_one(self):
        print("This is another method")

# __init__ is called automatically but any other methods inside the class you have to call them yourself
adam = Human() # object from a class
# adam.__init__()
# adam.__init__()
adam.another_one()