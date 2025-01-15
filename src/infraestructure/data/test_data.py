import datetime
from sqlmodel import Session
from src.domain.entities.departments import DepartmentBase
from src.domain.entities.employees import EmployeeBase
from src.domain.entities.spents import SpentsCreate
from src.infraestructure.database.database import get_session
from src.domain.entities.departments import DepartmentTable
from src.domain.entities.employees import EmployeeTable
from src.domain.entities.spents import SpentsTable
from random import randint

def generate_data():
    session = next(get_session()) 
    _generate_dep_data(session)
    _generate_employees_data(session)
    _generate_spents_data(session)
    session.close()

def _generate_dep_data(session: Session):
    for i in range(1, 50):
        dp = DepartmentTable(nombre=f"Departamento {i}")
        session.add(dp)
    session.commit()

def _generate_employees_data(session: Session):
    for i in range(1, 50):
        emp = EmployeeTable(nombre=f"Empleado {i}")
        session.add(emp)
    session.commit()

def _generate_spents_data(session: Session):
    for i in range(1, 75):
        spent = randint(100, 500000)
        day = randint(1, 28)
        month = randint(1, 12)
        year = randint(2020, 2023)
        id_emp = randint(1, 49)
        id_dep = randint(1, 49)
        fecha = datetime.date(year, month, day)
        spents = SpentsTable(
            monto=spent,
            fecha=fecha,
            descripcion=f"Gasto {i}",
            id_departamento=id_dep,
            id_empleado=id_emp,
        )
        session.add(spents)
    session.commit()