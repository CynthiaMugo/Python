# Problem
#  Given a number calculate the total of sum
# 5 = 5+4+3+2+1
# 10 = 

# big o - counting the number of operations
# operations = evry task that the computer does
import time

def calculate_sum(num):
    sum = 0 #operation a
    for number in range(1, num + 1): #operation b & c
        print(f"sum = {sum} , number = {number}") #operation d
        sum = sum + number #operation e
    print(f"For {num} The sum is {sum}") #operation f
    return sum #operation g

# a+b+c*(d+e)+g
# simplify =n
#n+n+n(n+n)+n
#3n(2n)+n
#6n^2+n
#n=1
#6+1
#10+2
#60000+100
# 6n^2-> 6(n^2)
# n^2 - big O notation of calculate_sum() this is equal to O(n)


def calculate_sum2(num):
    term1 = num + 1 #operation a
    term2 = num * term1 #operation b
    sum = term2 / 2 #operation c
    print(f"For {num} The sum is {sum}") #operation d
    return sum #operation e

# a+b+c+d+e
# 5n = n
# O(1)

start_time = time.time()
calculate_sum2(2345)
end_time = time.time()
diff = end_time - start_time
print(f"Speed {diff}")