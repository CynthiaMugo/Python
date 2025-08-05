import time

def time_fn(fn):
    def wrapper():
        start_time=time.time()
        fn()
        end_time=time.time()
        diff=end_time-start_time
        print("Time taken to run",diff)
    return wrapper

@time_fn
def counter():
    for n in range(0, 10000000):
        print(n)
counter()

def counter2():
    for n in range(0,10000):
        print(n)


start_time=time.time()
counter2()
end_time=time.time()

diff=end_time-start_time
print("counter2 function took ",diff)

@time_fn
def sum(*args):
    ans=0
    for n in args:
        # print(f"{ans}={ans}+{n}")
        print(ans,"=",ans,"+",n)
        ans=ans+n
    
    print("Ans is ",ans)
    return ans

sum(1,2,3,1000,10002,5345,34535,12234234,654645,23423)