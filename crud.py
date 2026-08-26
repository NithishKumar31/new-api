from sqlalchemy.orm import Session
import models, schemas

def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()
    if db_employee:
        update_data = employee.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_employee, key, value)
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
