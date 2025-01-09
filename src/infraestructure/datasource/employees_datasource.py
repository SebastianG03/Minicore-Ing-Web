from typing import Annotated
from fastapi import HTTPException, Query
from sqlmodel import Session, select

from src.domain.entities.employees import EmployeeBase, EmployeeTable

def get_employees(
    session: Session, 
    offset: int = 0, 
    limit: Annotated[int, Query(le=100)] = 100):
    employees = session.exec(select(EmployeeTable)
                             .offset(offset)
                             .limit(limit)).all()
    return employees

def get_employee(
    id: int,
    session: Session):
    employee = session.get(EmployeeTable, id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


def post_employee(employee: EmployeeBase, session: Session):
    employee_db = EmployeeTable(**employee.model_dump())
    session.add(employee_db)
    session.commit()
    session.refresh(employee_db)
    return employee_db

def patch_employee(id: int, employee: EmployeeBase, session: Session):
    emp_db: EmployeeTable = session.get(EmployeeTable, id)
    if not emp_db:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp_data = employee.model_dump(exclude_unset=True)
    emp_db.sqlmodel_update(emp_data)

    session.add(emp_db)
    session.commit()
    session.refresh(emp_db)
    return emp_db


def delete_employee(id: int, session: Session):
    employee = session.get(EmployeeTable, id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    session.delete(employee)
    session.commit()
    return {"message": f'Employee with id {id} was deleted'}
