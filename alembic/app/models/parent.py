from app import Base

from sqlalchemy import Column,String,BIGINT

class Parent(Base):

    __tablename__="parent"

    id=Column(BIGINT,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)