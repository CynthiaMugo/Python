from typing import List
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,Session
from sqlalchemy import Text,Boolean,select

from engine import engine


class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = 'employee'
    
    #columns 
    # colmns - static property
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str]=mapped_column(Text,nullable=False)
    email:Mapped[str]=mapped_column(Text,nullable=False,unique=True)

Base.metadata.create_all(engine)

with Session(engine) as session:
    # Create an employee
    # name="Malia"
    # email="malia@gmail.com"

    # emp=Employee(name=name,email=email)
    # session.add(emp)
    # session.commit()

    st_employess=select(Employee)

    #execute
    results=session.scalars(st_employess).all()

    for emp in results:
        print(f"name: {emp.name} email: {emp.email} id: {emp.id}")
        

    