from sqlmodel import SQLModel, Field
from pydantic import field_validator
from typing import Optional

class DepartmentBase(SQLModel):
    nombre: str = Field(max_length=100)

    @field_validator("nombre")
    def validate_nombre(cls, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        return value

class DepartmentTable(DepartmentBase, table=True):
    __tablename__ = "department"
    id: int = Field(default=None, index=True, primary_key=True, unique=True)
