from db import PG

class Employee:

    def __init__(self):
        # print("Initializing Employee class")
        pg = PG()
        # self.pg = pg
        query="""
            CREATE TABLE IF NOT EXISTS employee(
              id BIGSERIAL PRIMARY KEY,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE
            )
        """
        pg.pg_query(query=query)

    def add(self, name, email):
        pg = PG()
        query = """
            INSERT INTO employee(name, email)
            VALUES (%s, %s)
        """
        pg.pg_query(query=query, params=(name, email))
    def all(self):
        pg=PG()
        query="""
          SELECT * FROM employee
        """
        results=pg.pg_query(query=query)
        #print(results)
        for employee in results:
            print(employee)
        return

emp1 = Employee()
# emp1.add(name='Joan Sloan', email='sloan@gmail.com')

# name = input("Enter employee name: ")
# email = input("Enter employee email: ")
# emp1.add(name=name, email=email)
# print("Employee added successfully.")

# Adding with a loop to add multiple employees
# while True:
#     name=input("Enter employee name:")
#     email=input("Enter employee email:")
#     emp1.add(name=name,email=email)

#     print("Employee added ")
#     print("")
#     another=input("Enter y to add another ?:")
#     if another=="y" or another=="Y":
#         continue
#     break
# print("Exiting the employee addition process.")
  
emp1.all()  # Display all employees