"""
Практическое задание:
1. Протестируй health endpoint через `TestClient`.
2. Протестируй create endpoint через `TestClient`.
3. Проверь и `status_code`, и JSON-ответ.

Например:
- `GET /health` -> `200` и `{"status": "ok"}`
- `POST /jobs` -> `201` и `{"detail": "job created"}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI, status
from fastapi.testclient import TestClient

app = FastAPI(title='Practice Week 2 Day 3')


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@app.post('/jobs', status_code=status.HTTP_201_CREATED)
def create_job() -> dict[str, str]:
    return {'detail': 'job created'}


client = TestClient(app)


def test_health() -> None:
    response = client.get('/health')
    assert response.status_code == 200, 'expected 200 OK response'
    # TODO: замени placeholder на точный ожидаемый JSON.
    assert response.json() == {'status': 'TODO'}, 'health endpoint should return exact status ok payload'


def test_create_job() -> None:
    response = client.post('/jobs')
    assert response.status_code == 201, 'expected 201 Created response'
    # TODO: замени placeholder на точный ожидаемый JSON.
    assert response.json() == {'detail': 'TODO'}, 'POST /jobs should return creation payload'


def run_checks() -> None:
    test_health()
    test_create_job()


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
