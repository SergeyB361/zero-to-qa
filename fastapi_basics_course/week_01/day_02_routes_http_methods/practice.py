"""
Практическое задание:
1. Оставь корректный list route и detail route для пользователей.
2. Доделай `POST /users`, чтобы он возвращал осмысленный ответ создания.
3. Сохрани корректный `DELETE /users/{user_id}` контракт.

Например:
- `GET /users/1` -> `{"id": 1, "name": "Anna"}`
- `POST /users` -> `201` и что-то вроде `{"detail": "user created"}`
- `DELETE /users/2` -> `{"deleted_id": 2}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient

app = FastAPI(title='Practice Day 2')
users = [{'id': 1, 'name': 'Anna'}, {'id': 2, 'name': 'Boris'}]


@app.get('/users')
def list_users() -> list[dict[str, object]]:
    return users


@app.get('/users/{user_id}')
def get_user(user_id: int) -> dict[str, object]:
    for user in users:
        if user['id'] == user_id:
            return user
    raise HTTPException(status_code=404, detail='user not found')


@app.post('/users', status_code=status.HTTP_201_CREATED)
def create_user() -> dict[str, str]:
    return {'detail': 'TODO'}


@app.delete('/users/{user_id}')
def delete_user(user_id: int) -> dict[str, object]:
    return {'deleted_id': user_id}


client = TestClient(app)


def run_checks() -> None:
    response = client.get('/users')
    assert response.status_code == 200, 'expected 200 OK response'
    assert isinstance(response.json(), list), 'endpoint should return a JSON list'
    assert len(response.json()) >= 2, 'list endpoint should expose at least two seed items'

    response = client.get('/users/1')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json()['name'] == 'Anna', 'detail route should return seeded user Anna for id=1'

    response = client.get('/users/999')
    assert response.status_code == 404, 'expected 404 Not Found response'

    response = client.post('/users')
    assert response.status_code == 201, 'expected 201 Created response'
    assert response.json()['detail'] != 'TODO', 'detail field is still TODO'

    response = client.delete('/users/2')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == {'deleted_id': 2}, 'delete route should echo deleted_id=2'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
