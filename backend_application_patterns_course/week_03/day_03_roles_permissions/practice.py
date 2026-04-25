"""
Практическое задание:
1. Реализуй auth dependency по `X-API-Key`.
2. Реализуй permission dependency, которая пускает только `manager` и `admin`.
3. На недостаточных правах верни `403`.

Например:
- без API key -> `401`, `{"detail": "missing api key"}`
- viewer -> `403`, `{"detail": "insufficient permissions"}`
- manager -> `200`, `{"status": "report ready", "approved_by": "mila"}`

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



def get_actor_context(x_api_key: str | None = Header(default=None)) -> ActorContext:
    if x_api_key is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='missing api key')
    actor = TOKENS.get(x_api_key)
    if actor is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid api key')
    return actor



def require_manager_or_admin(actor: ActorContext = Depends(get_actor_context)) -> ActorContext:
    if actor.role not in ('manager', 'admin'):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='insufficient permissions')
    # TODO: вернуть actor без искажения контекста доступа.
    return ActorContext(actor_id='TODO', role=actor.role)


app = FastAPI(title='Backend Patterns Week 3 Day 3 Practice')


@app.get('/reports')
def reports(actor: ActorContext = Depends(require_manager_or_admin)) -> dict[str, str]:
    return {'status': 'report ready', 'approved_by': actor.actor_id}



def run_checks() -> None:
    client = TestClient(app)

    response = client.get('/reports')
    assert response.status_code == 401, 'missing api key should return 401'
    assert response.json() == {'detail': 'missing api key'}, 'missing api key detail is incorrect'

    response = client.get('/reports', headers={'X-API-Key': 'viewer-token'})
    assert response.status_code == 403, 'viewer should get 403 for protected report'
    assert response.json() == {'detail': 'insufficient permissions'}, 'forbidden detail is incorrect'

    response = client.get('/reports', headers={'X-API-Key': 'manager-token'})
    assert response.status_code == 200, 'manager should have access to report'
    assert response.json() == {'status': 'report ready', 'approved_by': 'mila'}, 'report payload is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
