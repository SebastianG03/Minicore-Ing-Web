# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.pool import StaticPool
# from sqlmodel import SQLModel

# from src.main import app
# from src.infraestructure.database.database import get_session
# from src.infraestructure.database.engine import engine
# from src.domain.entities.departments import Department

# # ========================
# # Configuración de la base de datos de prueba
# # ========================
# SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test_departments.db"

# # Crear motor de base de datos para pruebas
# test_engine = create_engine(
#     SQLALCHEMY_TEST_DATABASE_URL,
#     connect_args={"check_same_thread": False},
#     poolclass=StaticPool
# )

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# # Crear las tablas necesarias para las pruebas
# SQLModel.metadata.create_all(bind=test_engine)

# # Sobrescribir la dependencia de base de datos
# def override_get_session():
#     """Sobrescribe la dependencia de sesión para usar la base de datos de prueba."""
#     with TestingSessionLocal() as session:
#         yield session

# app.dependency_overrides[get_session] = override_get_session
# client = TestClient(app)

# # ========================
# # FIXTURES
# # ========================
# @pytest.fixture(scope="function")
# def db_session():
#     """Configura la sesión de base de datos con rollback al final."""
#     connection = test_engine.connect()
#     transaction = connection.begin()
#     session = TestingSessionLocal(bind=connection)
#     yield session
#     transaction.rollback()
#     connection.close()


# @pytest.fixture(scope="function")
# def test_client(db_session):
#     """Configura un cliente de prueba con la sesión de base de datos."""
#     def override_get_db():
#         try:
#             yield db_session
#         finally:
#             db_session.close()
    
#     app.dependency_overrides[get_session] = override_get_db
#     with TestClient(app) as client:
#         yield client


# @pytest.fixture()
# def valid_department_payload():
#     """Genera un payload válido para un departamento."""
#     return {"nombre": "Recursos Humanos"}


# @pytest.fixture()
# def invalid_department_payload():
#     """Genera un payload inválido para un departamento."""
#     return {"nombre": ""}


# # ========================
# # PRUEBAS UNITARIAS
# # ========================
# def test_get_all_departments(test_client, db_session):
#     """Prueba para obtener todos los departamentos."""
#     # Crear datos de prueba
#     department = Department(nombre="Departamento de Prueba")
#     db_session.add(department)
#     db_session.commit()

#     # Ejecutar prueba
#     response = test_client.get("/departments/all")
#     assert response.status_code == 200
#     departments = response.json()["departments"]
#     assert isinstance(departments, list)
#     assert len(departments) > 0
#     assert departments[0]["nombre"] == department.nombre


# def test_create_department(test_client, valid_department_payload):
#     """Prueba para crear un departamento."""
#     response = test_client.post("/departments/create", json=valid_department_payload)
#     assert response.status_code == 201
#     department = response.json()["department"]
#     assert department["nombre"] == valid_department_payload["nombre"]


# def test_create_invalid_department(test_client, invalid_department_payload):
#     """Prueba para intentar crear un departamento con datos inválidos."""
#     response = test_client.post("/departments/create", json=invalid_department_payload)
#     assert response.status_code == 422  # Código de estado para datos inválidos


# def test_update_department(test_client, db_session):
#     """Prueba para actualizar un departamento existente."""
#     # Crear un departamento para actualizar
#     department = Department(nombre="Departamento Antiguo")
#     db_session.add(department)
#     db_session.commit()
#     db_session.refresh(department)



# import pytest
# from httpx import AsyncClient
# from src.main import app  
# from src.domain.entities.departments import DepartmentBase

# @pytest.fixture
# def valid_department_data():
#     """Datos válidos para agregar un departamento."""
#     return {"nombre": "Recursos Humanos"}


# @pytest.fixture
# def invalid_department_data():
#     """Datos inválidos para agregar un departamento."""
#     return {"nombre": ""}


# @pytest.mark.asyncio
# async def test_get_all_departments():
#     """Prueba para obtener todos los departamentos."""
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         response = await client.get("/departments/all")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list), "La respuesta debe ser una lista de departamentos."


# @pytest.mark.asyncio
# async def test_post_valid_department(valid_department_data):
#     """Prueba para agregar un departamento con datos válidos."""
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         response = await client.post("/departments", json=valid_department_data)
#     assert response.status_code == 201, "Debe retornar 201 al crear exitosamente."
#     response_data = response.json()
#     assert response_data["nombre"] == valid_department_data["nombre"], "El nombre del departamento no coincide."


# @pytest.mark.asyncio
# async def test_post_invalid_department(invalid_department_data):
#     """Prueba para agregar un departamento con datos inválidos."""
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         response = await client.post("/departments", json=invalid_department_data)
#     assert response.status_code == 422, "Debe retornar 422 para datos inválidos."


# @pytest.mark.asyncio
# async def test_get_department_by_id():
#     """Prueba para obtener un departamento por ID."""
#     department_id = 1  # Ajustar según el contexto de pruebas
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         response = await client.get(f"/departments/{department_id}")
#     if response.status_code == 200:
#         assert response.json()["id"] == department_id, "El ID del departamento no coincide."
#     else:
#         assert response.status_code == 404, "Debe retornar 404 si el departamento no existe."


# @pytest.mark.asyncio
# async def test_update_department(valid_department_data):
#     """Prueba para actualizar un departamento existente."""
#     department_id = 1  # Ajustar según el contexto de pruebas
#     updated_data = {"nombre": "Updated Department"}
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         response = await client.patch(f"/departments/{department_id}", json=updated_data)
#     if response.status_code == 200:
#         response_data = response.json()
#         assert response_data["nombre"] == updated_data["nombre"], "El nombre del departamento no fue actualizado correctamente."
#     else:
#         assert response.status_code == 404, "Debe retornar 404 si el departamento no existe."


# @pytest.mark.asyncio
# async def test_delete_department():
#     """Prueba para eliminar un departamento por ID."""
#     department_id = 1  # Ajustar según el contexto de pruebas
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         response = await client.delete(f"/departments/{department_id}")
#     if response.status_code == 200:
#         response_data = response.json()
#         assert response_data["id"] == department_id, "El ID del departamento eliminado no coincide."
#     else:
#         assert response.status_code == 404, "Debe retornar 404 si el departamento no existe."
