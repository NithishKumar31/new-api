from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, get_db

# Create the database tables if they do not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employees API")

@app.post("/employees/", response_model=schemas.Employee, status_code=201)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, emp_id=employee.emp_id)
    if db_employee:
        raise HTTPException(status_code=400, detail="Employee ID already registered")
    return crud.create_employee(db=db, employee=employee)

@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees

@app.get("/employees/{emp_id}", response_model=schemas.Employee)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, emp_id=emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.put("/employees/{emp_id}", response_model=schemas.Employee)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id=emp_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, emp_id=emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
