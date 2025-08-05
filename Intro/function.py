## greets function <name> (parameters)

def greet(name, country):

    def inner():
        print("This is the inner function")

    outer()
    inner()
    print(name)
    print(country)
    print("Hi ",name, "Your favorite country is ",country)
    print(f"Hi {name} You want to travel to {country}")

def outer():
    print("This is the outer function")

greet("Sam", "Germany")
greet("Cynthia", "Ireland")