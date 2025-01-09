from fastapi import APIRouter, Depends

from src.domain.entities.employees import EmployeeBase
from src.infraestructure.database.database import get_session
import src.infraestructure.datasource.employees_datasource as dts

emp_router = APIRouter(prefix="/employees", tags=["employees"])

@emp_router.get("/all")
def get_all_employees(session=Depends(get_session)):
    return dts.get_employees(session=session)

@emp_router.get("/{id}")
def get_employees(id: int, session=Depends(get_session)):
    return dts.get_employee(id=id, session=session)

@emp_router.post("/post")
def post_employees(employee: EmployeeBase, session=Depends(get_session)):
    return dts.post_employee(employee=employee, session=session)

@emp_router.patch("/update/{id}")
def update_employees(employee: EmployeeBase, id: int, session=Depends(get_session)):
    return dts.patch_employee(id=id, employee=employee, session=session)

@emp_router.delete("/delete/{id}")
def delete_employees(id: int, session=Depends(get_session)):
    return dts.delete_employee(id=id, session=session)