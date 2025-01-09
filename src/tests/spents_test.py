import pytest
from httpx import AsyncClient
from datetime import date, timedelta
from src.main import app  # Ajusta este import según tu estructura
from src.domain.entities.spents import SpentsCreate, SpentsUpdate


# Fixtures para datos de prueba
@pytest.fixture
def valid_spent_data():
    return {
        "fecha": str(date.today() - timedelta(days=1)),
        "descripcion": "Compra de equipo",
        "monto": 100.50,
        "id_empleado": 1,
        "id_departamento": 1,
    }


@pytest.fixture
def invalid_spent_data():
    return {
        "fecha": str(date.today() + timedelta(days=1)),  # Fecha futura
        "descripcion": "",  # Descripción vacía
        "monto": -50.0,  # Monto negativo
        "id_empleado": 1,
        "id_departamento": 1,
    }


@pytest.mark.asyncio
async def test_get_all_spents():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/spents/all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_spents_by_id():
    spent_id = 1  # Ajusta según datos de prueba o mocks
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get(f"/spents/{spent_id}")
    if response.status_code == 200:
        assert response.json()["id"] == spent_id
    else:
        assert response.status_code == 404


@pytest.mark.asyncio
async def test_post_valid_spents(valid_spent_data):
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/spents/post", json=valid_spent_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["descripcion"] == valid_spent_data["descripcion"]
    assert response_data["monto"] == valid_spent_data["monto"]


@pytest.mark.asyncio
async def test_post_invalid_spents(invalid_spent_data):
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/spents/post", json=invalid_spent_data)
    assert response.status_code == 422  # Error de validación


@pytest.mark.asyncio
async def test_update_spents(valid_spent_data):
    spent_id = 1  # Ajusta para la base de datos de prueba
    updated_data = {
        "fecha": str(date.today() - timedelta(days=2)),
        "descripcion": "Actualización de gasto",
        "monto": 200.75,
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.patch(f"/spents/update/{spent_id}", json=updated_data)
    if response.status_code == 200:
        assert response.json()["descripcion"] == updated_data["descripcion"]
        assert response.json()["monto"] == updated_data["monto"]
    else:
        assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_spents():
    spent_id = 1  # Ajusta según datos de prueba
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete(f"/spents/delete/{spent_id}")
    if response.status_code == 200:
        assert response.json()["id"] == spent_id
    else:
        assert response.status_code == 404
