"""
Практическое задание:
1. Реализуй dependency, которая читает `Authorization: Bearer ...`.
2. Верни actor context для валидного token.
3. На missing/invalid token верни `401`.

Например:
- без header -> `401`, `{"detail": "missing bearer token"}`
- `Bearer manager-token` -> `200`, `{"actor_id": "mila", "role": "manager"}`
- `Bearer wrong` -> `401`, `{"detail": "invalid bearer token"}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from dataclasses import dataclass

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.testclient import TestClient


@dataclass(slots=True)
class ActorContext:
    actor_id: str
    role: str


TOKENS = {
    'manager-token': ActorContext(actor_id='mila', role='manager'),
    'viewer-token': ActorContext(actor_id='nik', role='viewer'),
}



def get_actor_context(authorization: str | None = Header(default=None)) -> ActorContext:
    if authorization is None or not authorization.startswith('Bearer '):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='missing bearer token')

    token = authorization.removeprefix('Bearer ').strip()
    if token not in TOKENS:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid bearer token')

    # TODO: вернуть ActorContext из TOKENS для валидного token.
    return ActorContext(actor_id='TODO', role='TODO')


app = FastAPI(title='Backend Patterns Week 3 Day 1 Practice')


@app.get('/me')
def me(actor: ActorContext = Depends(get_actor_context)) -> dict[str, str]:
    return {'actor_id': actor.actor_id, 'role': actor.role}



def run_checks() -> None:
    client = TestClient(app)

    response = client.get('/me')
    assert response.status_code == 401, 'missing token should return 401'
    assert response.json() == {'detail': 'missing bearer token'}, 'missing token detail is incorrect'

    response = client.get('/me', headers={'Authorization': 'Bearer manager-token'})
    assert response.status_code == 200, 'valid token should return 200'
    assert response.json() == {'actor_id': 'mila', 'role': 'manager'}, 'actor context payload is incorrect'

    response = client.get('/me', headers={'Authorization': 'Bearer wrong'})
    assert response.status_code == 401, 'invalid token should return 401'
    assert response.json() == {'detail': 'invalid bearer token'}, 'invalid token detail is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
