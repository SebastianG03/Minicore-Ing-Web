from sqlmodel import Relationship, SQLModel, Field
from pydantic import field_validator
from datetime import date
from typing import Optional

from src.domain.entities.departments import DepartmentTable
from src.domain.entities.employees import EmployeeTable

class SpentsBase(SQLModel):
    fecha: date
    descripcion: str = Field(max_length=100)
    monto: float
    
    
class SpentsCreate(SQLModel):
    fecha: date
    descripcion: str = Field(max_length=100)
    monto: float
    id_empleado: int
    id_departamento: int

class SpentsUpdate(SQLModel):
    fecha: Optional[date]
    descripcion: Optional[str] = Field(max_length=100)
    monto: Optional[float]
    id_empleado: Optional[int]
    id_departamento: Optional[int]


class SpentsTable(SpentsBase, table=True):
    __tablename__ = "spents"
    id: int = Field(default=None, primary_key=True, index=True)
    id_empleado: int = Field(foreign_key="employee.id")
    id_departamento: int = Field(foreign_key="department.id")
    
    # empleado: "EmployeeTable" = Relationship(back_populates="spents")
    # departamento: "DepartmentTable" = Relationship(back_populates="spents")

    @field_validator("descripcion")
    def validate_descripcion(cls, value):
        if not value.strip():
            raise ValueError("La descripción no puede estar vacía.")
        return value

    @field_validator("monto")
    def validate_monto(cls, value):
        if value <= 0:
            raise ValueError("El monto debe ser mayor a 0.")
        return value

    @field_validator("fecha")
    def validate_fecha(cls, value):
        if value > date.today():
            raise ValueError("Debe ingresar una fecha menor a la actual.")
        return value

