"""
Практическое задание:
1. Подключи тесты к `backend_service_capstone.create_app`.
2. Покрой health, auth, create, patch и soft delete.
3. Не тестируй implementation details repository/service напрямую.

Критерий готовности: `pytest test_backend_service.py` проходит.
"""

from fastapi.testclient import TestClient

from backend_service_capstone import create_app


def build_client() -> TestClient:
    return TestClient(create_app())


def test_health() -> None:
    client = build_client()

    response = client.get('/health')

    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_missing_credentials_are_rejected() -> None:
    client = build_client()

    response = client.get('/items')

    assert response.status_code == 401


def test_manager_create_patch_and_soft_delete_flow() -> None:
    client = build_client()

    create_response = client.post(
        '/items',
        headers={'X-API-Key': 'manager-token'},
        json={'name': 'Portal'},
    )

    assert create_response.status_code == 201
    # TODO: после реализации service layer ожидается {'id': 1, 'name': 'Portal', 'status': 'draft'}.
    assert create_response.json() == {'id': 1, 'name': 'Portal', 'status': 'draft'}

    patch_response = client.patch(
        '/items/1',
        headers={'X-API-Key': 'manager-token'},
        json={'status': 'active'},
    )

    assert patch_response.status_code == 200
    assert patch_response.json() == {'id': 1, 'name': 'Portal', 'status': 'active'}

    delete_response = client.delete('/items/1', headers={'X-API-Key': 'manager-token'})

    assert delete_response.status_code == 204

    get_response = client.get('/items/1', headers={'X-API-Key': 'viewer-token'})

    assert get_response.status_code == 404


def test_viewer_cannot_create_item() -> None:
    client = build_client()

    response = client.post(
        '/items',
        headers={'X-API-Key': 'viewer-token'},
        json={'name': 'Portal'},
    )

    assert response.status_code == 403
