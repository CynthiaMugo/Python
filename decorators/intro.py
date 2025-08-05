# Decorators
## Extend or modify the behaviour of 
## functions or without changing their code
## CALLBACKS<-->

def my_deco(func):
    def wrapper():
        print("Before function run")
        func()
        print("function completed running")
    return wrapper

@my_deco
def hello():
    print("Hello world")

# my_deco(func=hello)()
hello()

# @my_deco
def greet():
    print("Greetings from above")
greet()
my_deco(greet)()