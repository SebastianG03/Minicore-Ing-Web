from contextlib import asynccontextmanager
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import FastAPI

from src.infraestructure.database.database import create_tables
from src.application.controllers.departments_controller import dep_router
from src.application.controllers.employees_controller import emp_router
from src.application.controllers.spents_controller import spents_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

def create_app():
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(GZipMiddleware)
    app.include_router(dep_router)
    app.include_router(spents_router)
    app.include_router(emp_router)
    return app

app = create_app()
