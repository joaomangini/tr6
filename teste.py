import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calcular_adicao(client):
    payload = {
        "valor": 10,
        "valor2": 5,
        "operacao": "adicao"
    }
    response = client.post('/calcular', json=payload)
    data = response.get_json()
    assert response.status_code == 200
    assert data['resultado'] == 15

def test_calcular_divisao_por_zero(client):
    payload = {
        "valor": 10,
        "valor2": 0,
        "operacao": "divisao"
    }
    response = client.post('/calcular', json=payload)
    data = response.get_json()
    assert response.status_code == 400
    assert "Divisão por zero não é permitida" in data['mensagem']