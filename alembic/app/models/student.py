from app import Base

from sqlalchemy import Column, Integer, String, BIGINT

class Student(Base):
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    admission_number = Column(BIGINT, unique=True, nullable=False)
    
    