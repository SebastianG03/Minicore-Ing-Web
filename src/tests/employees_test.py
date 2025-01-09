import pytest
from httpx import AsyncClient
from src.main import app  
from src.domain.entities.employees import EmployeeBase


# Fixtures para datos de prueba
@pytest.fixture
def valid_employee_data():
    return {"nombre": "Juan Pérez"}


@pytest.fixture
def invalid_employee_data():
    return {"nombre": ""}


# Prueba para obtener todos los empleados
@pytest.mark.asyncio
async def test_get_all_employees():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/employees/all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Prueba para obtener un empleado por ID
@pytest.mark.asyncio
async def test_get_employee_by_id():
    employee_id = 1  # Ajusta este ID según la base de datos de prueba o mocks
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get(f"/employees/{employee_id}")
    if response.status_code == 200:
        assert response.json()["id"] == employee_id
    else:
        assert response.status_code == 404


# Prueba para crear un empleado con datos válidos
@pytest.mark.asyncio
async def test_post_valid_employee(valid_employee_data):
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/employees/post", json=valid_employee_data)
    assert response.status_code == 200
    assert response.json()["nombre"] == valid_employee_data["nombre"]


# Prueba para crear un empleado con datos inválidos
@pytest.mark.asyncio
async def test_post_invalid_employee(invalid_employee_data):
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/employees/post", json=invalid_employee_data)
    assert response.status_code == 422  # Error de validación


# Prueba para actualizar un empleado
@pytest.mark.asyncio
async def test_update_employee(valid_employee_data):
    employee_id = 1  # Ajusta para la base de datos de prueba
    updated_data = {"nombre": "Actualizado Pérez"}
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.patch(f"/employees/update/{employee_id}", json=updated_data)
    if response.status_code == 200:
        assert response.json()["nombre"] == updated_data["nombre"]
    else:
        assert response.status_code == 404


# Prueba para eliminar un empleado
@pytest.mark.asyncio
async def test_delete_employee():
    employee_id = 1  # Ajusta según datos de prueba
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete(f"/employees/delete/{employee_id}")
    if response.status_code == 200:
        assert response.json()["id"] == employee_id
    else:
        assert response.status_code == 404
