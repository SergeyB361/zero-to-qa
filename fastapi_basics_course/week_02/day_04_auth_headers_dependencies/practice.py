"""
Практическое задание:
1. Оформи auth-check как dependency, а не как логику route.
2. Для неверного токена верни `401`.
3. Для правильного токена верни успешный protected response.

Например:
- без `x-actor-token` -> `401` и `{"detail": "invalid actor token"}`
- с `x-actor-token: qa-demo-token` -> `200` и `{"detail": "protected tasks list", "token": "qa-demo-token"}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.testclient import TestClient

app = FastAPI(title='Practice Week 2 Day 4')


def require_actor_token(x_actor_token: Annotated[str | None, Header()] = None) -> str:
    if x_actor_token != 'qa-demo-token':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='TODO')
    # TODO: верни реальный токен из header, а не placeholder.
    return 'TODO'


@app.get('/admin/tasks')
def admin_tasks(token: Annotated[str, Depends(require_actor_token)]) -> dict[str, str]:
    # TODO: верни осмысленный protected response.
    return {'detail': 'TODO', 'token': token}


client = TestClient(app)


def run_checks() -> None:
    response = client.get('/admin/tasks')
    assert response.status_code == 401, 'expected 401 Unauthorized response'
    assert response.json()['detail'] == 'invalid actor token', 'bad token branch should explain the auth failure'

    response = client.get('/admin/tasks', headers={'x-actor-token': 'qa-demo-token'})
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == {'detail': 'protected tasks list', 'token': 'qa-demo-token'}, 'authorized response payload is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
