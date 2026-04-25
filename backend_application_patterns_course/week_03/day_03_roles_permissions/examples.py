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


def get_actor_context(x_api_key: str | None = Header(default=None)) -> ActorContext:
    if x_api_key is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='missing api key')
    actor = TOKENS.get(x_api_key)
    if actor is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid api key')
    return actor



def require_roles(*roles: str):
    def dependency(actor: ActorContext = Depends(get_actor_context)) -> ActorContext:
        if actor.role not in roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='insufficient permissions')
        return actor

    return dependency


app = FastAPI(title='Backend Patterns Week 3 Day 3')


@app.get('/reports')
def reports(_: ActorContext = Depends(require_roles('admin', 'manager'))) -> dict[str, str]:
    return {'report': 'top-level metrics'}


if __name__ == '__main__':
    client = TestClient(app)
    print('VIEWER ->', client.get('/reports', headers={'X-API-Key': 'viewer-token'}).status_code)
    print('ADMIN ->', client.get('/reports', headers={'X-API-Key': 'admin-token'}).status_code, client.get('/reports', headers={'X-API-Key': 'admin-token'}).json())
