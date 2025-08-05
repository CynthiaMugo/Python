# your function only takes 3 parameters
# your function 4 or 5 or 6
#Args -> arguments
#def stuff(name,age,gender,is_married):

# parametrs<fixed> how many of taken

# def greet(person1,person2,person3):
#     print("Name is",person1)
#     print("Name is",person2)
#     print("Name is",person3)

def greet(*args):

    print(*args)
    for arg in args:
        print("Name is", arg)

greet("John", "Samuel", "Cynthia")

def sum(*args):
    ans = 0
    for n in args:
        print(f"{ans}={ans}+{n}")
        ans=ans+n
        
    print("Ans is",ans)
    return ans

sum(100,50,20,30,150,200,700)