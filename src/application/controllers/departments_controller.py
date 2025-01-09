from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.domain.entities.departments import DepartmentBase
from src.infraestructure.database.database import get_session
import src.infraestructure.datasource.departments_datasource as dts

dep_router = APIRouter(prefix="/departments", tags=["departments"])


@dep_router.get("/all")
def get_all_departments(session=Depends(get_session)):
    try:
        return dts.get_departments(session)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@dep_router.get("/{id}")
def get_department_by_id(id: int, session=Depends(get_session)):
    try:
        return dts.get_department_by_id(id=id, session=session)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@dep_router.post("/post")
def post_department(department: DepartmentBase, session=Depends(get_session)):
    try:
        return dts.post_departments(department=department, session=session)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@dep_router.patch("/update/{id}")
def update_department(department: DepartmentBase, id: int, session=Depends(get_session)):
    try:
        return dts.put_departments(id=id, department=department, session=session)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@dep_router.delete("/delete/{id}")
def delete_department(id: int, session=Depends(get_session)):
    try:
        return dts.delete_departments(id=id, session=session)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
