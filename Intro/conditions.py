# if, else if, else
age = 20

if age > 21:
    print("You can drink")
else:
    print("You are under age")

# 0 and 12
# && - and || - or
if age < 12:
    print("You are a baby")
elif age >= 12 and age < 18:
    print("You are anadolescent")
elif age >= 18 and age < 21:
    print("Imagine people were drinking at this age")
elif age >= 21:
    print("Legal drinking age")
else:
    print("Sth else")