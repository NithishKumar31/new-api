from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    emp_name: str
    department: str
    salary: int

class EmployeeCreate(EmployeeBase):
    emp_id: int

class EmployeeUpdate(BaseModel):
    emp_name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[int] = None

class Employee(EmployeeBase):
    emp_id: int

    class Config:
        orm_mode = True
