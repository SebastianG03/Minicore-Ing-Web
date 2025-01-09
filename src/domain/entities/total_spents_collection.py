from typing import Optional
from pydantic import BaseModel


class TotalSpent(BaseModel):
    id_departamento: int | None
    nombre_departamento: str = ""
    gasto_total: float
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed=True
        
    