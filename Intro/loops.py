# for, while, do_while
to_loop = True
i = 0

while to_loop:
    if i > 10:
        to_loop = False
    print("i is", i)
    i = i + 1

k = 0

while k < 10:
    print("k is", k)
    k = k + 1

#for(starting condition)
#for(let i=0;i<10;i++)
# starting from 2 to 10
for i in range(2, 10):
    print("For i in this loop is", i)

# starting from 10 to 2
for i in range(10, 2, -1):
    print("For i in this loop is", i)

for i in range(0, 40, 2):
   print("All even numbers", i)