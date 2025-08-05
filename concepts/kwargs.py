## *kwargs -> Key word arguments
## Dictionary{key:value}
def greet(name, nationality):
    print("Name is", name)
    print("From", nationality)

#kwargs solves mixups to specify each variable in the function
greet(nationality="India", name="Kamala")

# Kwargs profile
def employee(**kwargs):
    print(kwargs)
    print(kwargs.items())
    for key,value in kwargs.items():
        print("For key",key, "The value is",value)

employee(name="Terry", age=20, degree="engineering")
employee(name="Tulsa", age=22, country="Kenya", degree="medicine")

def do_drink(**kwargs):
    drinks=kwargs["drink"]
    prices=kwargs["prices"]

    print(kwargs)

    for index,value in enumerate(drinks):
        print("For index",index)
        print("The Drink",value)
        print("The price",prices[index])


##ARGS AND KWARGS --> DECORATORS
do_drink(drink=["Glenfidish","KingFisher"],
         prices=[120,100,40])

def mixed(*args,**kwargs):
    print("Kwargs",kwargs)
    print("Args",args)

mixed("cool","drinks",name="John",age=20,)

def square_all(*args):
    ans=[]
    for n in args:
        ans.append(n*n)
    print(ans)
    return ans

square_all(2,4,6,1)