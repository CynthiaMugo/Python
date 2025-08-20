from lite import LITE

class Employee():

    def __init__(self):
        lite=LITE()
        
        query="""
            CREATE TABLE IF NOT EXISTS employee(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE
            )
        """
        lite.lite_query(query=query)
    
    def add(self,name,email):
        lite=LITE()
        query="""
          INSERT INTO employee
          (name,email)
          VALUES  (?,?)
        """

        lite.lite_query(query=query,params=(name,email))

    def all(self):
        lite=LITE()
        query="""
          SELECT * FROM employee
        """
        results=lite.lite_query(query=query)
        #print(results)
        for employee in results:
            print(employee)
        return
    

emp1=Employee()

## CREATE OTHER CLASSES
## CRUD ->  Create Read Update Delete
## sqlite

#create an employee (C)
#all employees (R)
#Update 
#Delete
# emp1.add(name="Marry",email="marry@gmail.com")

while True:
    name=input("Enter employee name:")
    email=input("Enter employee email:")
    emp1.add(name=name,email=email)

    print("Employee added ")
    print("")
    print("All employees:")
    emp1.all()
    print("--------------------------------------")
    another=input("Enter y to add another ?:")
    if another=="y" or another=="Y":
        continue
    break

# READ, READ. UPDATE()

# emp1.all()