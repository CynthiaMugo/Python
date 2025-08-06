import time

def logger(func):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        func(*args,**kwargs) # will run
        end_time=time.time()
        diff=end_time-start_time
        txt=f"function:{func.__name__} time taken {diff} seconds"
        f_name="logger.txt"
        write_file(f_name=f_name,txt=txt)
    return wrapper

def write_file(f_name, txt):
    with open(f_name, "a") as file:
        file.write(f"{txt} \n")

write_file(f_name="logger.txt", txt="Hello, Cynthia")

@logger
def counter():
    for n in range(0,10000000):
        print(n)
# counter()

@logger
def sum(*args):
    ans=0
    for n in args:
        # print(f"{ans}={ans}+{n}")
        print(ans,"=",ans,"+",n)
        ans=ans+n
    
    print("Ans is ",ans)
    return ans

sum(100,2004,500,345,6767,457546)