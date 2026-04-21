"""
Практическое задание:
1. Сделай корневой endpoint осмысленным, а не с `TODO`.
2. Верни корректный health response `{"status": "ok"}`.
3. Заполни meta-информацию о сервисе.

Например:
- `GET /` -> `{"message": "fastapi basics service"}`
- `GET /health` -> `{"status": "ok"}`
- `GET /meta` -> `{"service": "fastapi-basics", "version": "1.0"}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI(title='Practice Day 1')


@app.get('/')
def read_root() -> dict[str, str]:
    return {'message': 'TODO'}


@app.get('/health')
def healthcheck() -> dict[str, str]:
    return {'status': 'TODO'}


@app.get('/meta')
def meta() -> dict[str, str]:
    return {'service': 'TODO', 'version': 'TODO'}


client = TestClient(app)


def run_checks() -> None:
    response = client.get('/')
    assert response.status_code == 200, 'expected 200 OK response'
    body = response.json()
    assert body['message'] != 'TODO', 'root message is still TODO'
    assert len(body['message'].strip()) >= 4, 'root message is too short to be meaningful'

    response = client.get('/health')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == {'status': 'ok'}, 'health endpoint should return exact status ok payload'

    response = client.get('/meta')
    assert response.status_code == 200, 'expected 200 OK response'
    body = response.json()
    assert body['service'] != 'TODO', 'service field is still TODO'
    assert body['version'] != 'TODO', 'version field is still TODO'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
