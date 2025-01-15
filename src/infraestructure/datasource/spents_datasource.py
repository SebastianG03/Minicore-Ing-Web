from datetime import date
from typing import Annotated
from fastapi import HTTPException, Query
from sqlmodel import Session, select

from src.domain.entities.spents import SpentsTable, SpentsCreate, SpentsUpdate
from src.domain.entities.total_spents_collection import TotalSpent
from src.domain.entities.departments import DepartmentTable

def get_spents(
    session: Session, 
    offset: int = 0, 
    limit: Annotated[int, Query(le=100)] = 100):
    spents = session.exec(select(SpentsTable)
                          .offset(offset)
                          .limit(limit)).all()
    return spents

def get_spent(
    id: int,
    session: Session):
    spent = session.get(SpentsTable, id)
    if not spent:
        raise HTTPException(status_code=404, detail="Spent not found")
    return spent


def post_spent(spent: SpentsCreate, session: Session):
    spent_db = SpentsTable(**spent.model_dump(exclude_unset=True))
    session.add(spent_db)
    session.commit()
    session.refresh(spent_db)
    return spent_db

def patch_spent(id: int, spent: SpentsUpdate, session: Session):
    spent_db: SpentsTable = session.get(SpentsTable, id)
    if not spent_db:
        raise HTTPException(status_code=404, detail="Spent not found")
    spent_data = spent.model_dump(exclude_unset=True)
    spent_db.sqlmodel_update(spent_data)

    session.add(spent_db)
    session.commit()
    session.refresh(spent_db)
    return spent_db


def delete_spent(id: int, session: Session):
    spent = session.get(SpentsTable, id)
    if not spent:
        raise HTTPException(status_code=404, detail="Spent not found")
    session.delete(spent)
    session.commit()
    return {"message": f'Spent with id {id} was deleted'}
def calculate_spents_by_dates(begin: date, end: date, session: Session):
    spents = session.exec(
        select(SpentsTable)
        .where(SpentsTable.fecha.between(begin, end))
        ).all()
    
    spents_by_department: dict = {}
    
    for spent in spents:
        total_spent = TotalSpent(
            id_departamento=spent.id_departamento,
            gasto_total=spent.monto
        )
        if total_spent.id_departamento not in spents_by_department:
            spents_by_department.update({total_spent.id_departamento: total_spent})
        else:
            spents_by_department[total_spent.id_departamento].gasto_total += total_spent.gasto_total
    
    for spent in spents_by_department.values():
        department = session.get(DepartmentTable, spent.id_departamento)
        spent.nombre_departamento = department.nombre
        spent.id_departamento = None
    
    
    return [spent.model_dump(exclude_unset=True, exclude_none=True) for spent in spents_by_department.values()]