from dataclasses import dataclass

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.testclient import TestClient


@dataclass(slots=True)
class ActorContext:
    actor_id: str
    role: str


TOKENS = {
    'admin-token': ActorContext(actor_id='anna', role='admin'),
    'viewer-token': ActorContext(actor_id='boris', role='viewer'),
}


def get_actor_context(authorization: str | None = Header(default=None)) -> ActorContext:
    if authorization is None or not authorization.startswith('Bearer '):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='missing bearer token')

    token = authorization.removeprefix('Bearer ').strip()
    actor = TOKENS.get(token)
    if actor is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid bearer token')
    return actor


app = FastAPI(title='Backend Patterns Week 3 Day 1')


@app.get('/me')
def me(actor: ActorContext = Depends(get_actor_context)) -> dict[str, str]:
    return {'actor_id': actor.actor_id, 'role': actor.role}


if __name__ == '__main__':
    client = TestClient(app)
    print('MISSING TOKEN ->', client.get('/me').status_code, client.get('/me').json())
    print(
        'VALID TOKEN ->',
        client.get('/me', headers={'Authorization': 'Bearer admin-token'}).status_code,
        client.get('/me', headers={'Authorization': 'Bearer admin-token'}).json(),
    )
