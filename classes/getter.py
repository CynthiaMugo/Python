
#initializer:constructor

#Speical method in a class
#initializer: method is called whenver the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to hhave thhe self: keyworkd

#how to create a class <-->What a class is
# initialiZer <constrocture>
# self key what it is :<this>

from datetime import datetime

def write_file(f_name, txt):
        with open(f_name,'a') as file:
            file.write(f"{txt} \n")

class Human():
    def __init__(self,gender,name):
        print("The initializer was called")
        self.gender=gender
        self._name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"

    @property
    def name(self):
        print("Somebody wants to get the name of a property")
        now = datetime.now()
        print("Current date and time", now)
        write_file(f_name="log.txt", txt=f"At {now} got name from adam")
        return self._name
    
    def print_self(self):
        print("----------------------")
        print("name",self.name)
        print("gender",self.gender)
        print("ribs",self.ribs)
        print("curse",self.curse)
        print("---------------------")


# adam=Human(name="adam",gender="Male") #object from a class
adam=Human(name="adam",gender="Male")
# adam.print_self()

# Get data from an object
print(adam.name)

# getting data or reading data

# Getters and Setters ----> Security ---> Like Decorator -->modify when tries to get
# Control how the data is gotten.

# employee-> salary -> modified when its being modified