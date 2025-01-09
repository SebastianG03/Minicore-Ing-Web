from typing import Annotated
from fastapi import HTTPException, Query
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

from src.domain.entities.departments import DepartmentBase, DepartmentTable


def get_departments(
    session: Session, 
    offset: int = 0, 
    limit: Annotated[int, Query(le=100)] = 100):
    deps = session.exec(select(DepartmentTable)
                        .offset(offset)
                        .limit(limit)).all()
    return deps

def get_department_by_id(
    id: int,
    session: Session):
    dep = session.get(DepartmentTable, id)
    if not dep:
        raise HTTPException(status_code=404, detail="Department not found")
    return dep
    


def post_departments(department: DepartmentBase, session: Session):
    department_db = DepartmentTable.model_validate(department)
    session.add(department_db)
    session.commit()
    session.refresh(department_db)
    return department_db

def put_departments(id: int, department: DepartmentBase, session: Session):
    dep_db: DepartmentTable = session.get(DepartmentTable, id)
    if not dep_db:
        raise HTTPException(status_code=404, detail="Department not found")
    dep_data = department.model_dump(exclude_unset=True)
    dep_db.sqlmodel_update(dep_data)
    
    session.add(dep_db)
    session.commit()
    session.refresh(dep_db)
    return dep_db
    

def delete_departments(id: int, session: Session):
    dep = session.get(DepartmentTable, id)
    if not dep:
        raise HTTPException(status_code=404, detail="Department not found")
    session.delete(dep)
    session.commit()
    return {"message": f'Department with id {id} was deleted'}