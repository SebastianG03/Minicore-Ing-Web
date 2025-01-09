from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.infraestructure.database.database import get_session
from src.domain.entities.spents import  SpentsUpdate, SpentsCreate
import src.infraestructure.datasource.spents_datasource as dts 

spents_router = APIRouter(prefix="/spents", tags=["spents"])

@spents_router.get("/all")
def get_all_spents(session=Depends(get_session)):
    return dts.get_spents(session=session)

@spents_router.get("/{id}")
def get_spents_by_id(id: int, session=Depends(get_session)):
    return dts.get_spent(id=id, session=session)

@spents_router.post("/post")
def post_spents(spents: SpentsCreate, session=Depends(get_session)):
    return dts.post_spent(spent=spents, session=session)

@spents_router.patch("/update/{id}")
def update_spents(spents: SpentsUpdate, spent_id: int, session=Depends(get_session)):
    return dts.patch_spent(id=spent_id, spent=spents, session=session)

@spents_router.delete("/delete/{id}")
def delete_spents(id: int, session=Depends(get_session)):
    return dts.delete_spent(id=id, session=session)

@spents_router.get("/total-gastos/{inicio}/{fin}")
def calculate_total_spents(inicio: date, fin: date, session=Depends(get_session)):
    if inicio > fin:
        return HTTPException(status_code=400, detail="La fecha de inicio debe ser anterior o igual a la fecha de fin.")
    return JSONResponse( content= dts.calculate_spents_by_dates(begin=inicio, end=fin, session=session))