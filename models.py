from sqlalchemy import Column, Integer, String
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String(50), index=True)
    department = Column(String(50), index=True)
    salary = Column(Integer)
