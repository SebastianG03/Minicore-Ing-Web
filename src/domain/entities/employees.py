from sqlmodel import SQLModel, Field
from pydantic import field_validator
from typing import Optional


class EmployeeBase(SQLModel):
    nombre: str = Field(max_length=50)

    @field_validator("nombre")
    def validate_nombre(cls, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        return value

class EmployeeTable(EmployeeBase, table=True):
    __tablename__ = "employee"
    id: int = Field(default=None, index=True, primary_key=True)