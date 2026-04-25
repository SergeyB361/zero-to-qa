"""
Практическое задание:
1. Собери auth + role check + business rule в один service flow.
2. Раздели `403` за недостаточные права и `409` за доменный конфликт.
3. Разреши закрывать incident только manager-у и только один раз.

Например:
- viewer -> `403`, `{"detail": "insufficient permissions"}`
- manager first close -> `200`, `{"id": 1, "title": "checkout fails", "status": "closed"}`
- manager second close -> `409`, `{"detail": "incident already closed"}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from dataclasses import dataclass

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.testclient import TestClient


@dataclass(slots=True)
class ActorContext:
    actor_id: str
    role: str


TOKENS = {
    'manager-token': ActorContext(actor_id='mila', role='manager'),
    'viewer-token': ActorContext(actor_id='nik', role='viewer'),
}
INCIDENTS = [{'id': 1, 'title': 'checkout fails', 'status': 'open'}]


class IncidentAlreadyClosedError(RuntimeError):
    pass



def get_actor_context(x_api_key: str | None = Header(default=None)) -> ActorContext:
    if x_api_key is None:
        raise HTTPException(status_code=401, detail='missing api key')
    actor = TOKENS.get(x_api_key)
    if actor is None:
        raise HTTPException(status_code=401, detail='invalid api key')
    return actor



def require_manager(actor: ActorContext = Depends(get_actor_context)) -> ActorContext:
    if actor.role != 'manager':
        raise HTTPException(status_code=403, detail='insufficient permissions')
    return actor


class IncidentService:
    def close_incident(self, incident_id: int) -> dict[str, object]:
        incident = next((item for item in INCIDENTS if item['id'] == incident_id), None)
        if incident is None:
            raise HTTPException(status_code=404, detail='incident not found')
        # TODO: запретить повторное закрытие через IncidentAlreadyClosedError.
        return {'id': incident['id'], 'title': incident['title'], 'status': 'TODO'}


app = FastAPI(title='Backend Patterns Week 3 Day 6 Practice')
service = IncidentService()


@app.patch('/incidents/{incident_id}/close')
def close_incident(incident_id: int, _: ActorContext = Depends(require_manager)) -> dict[str, object]:
    try:
        return service.close_incident(incident_id)
    except IncidentAlreadyClosedError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc



def run_checks() -> None:
    client = TestClient(app)

    response = client.patch('/incidents/1/close', headers={'X-API-Key': 'viewer-token'})
    assert response.status_code == 403, 'viewer should get 403 for close action'
    assert response.json() == {'detail': 'insufficient permissions'}, 'viewer forbidden detail is incorrect'

    response = client.patch('/incidents/1/close', headers={'X-API-Key': 'manager-token'})
    assert response.status_code == 200, 'manager should be able to close open incident'
    assert response.json() == {'id': 1, 'title': 'checkout fails', 'status': 'closed'}, 'first close payload is incorrect'

    response = client.patch('/incidents/1/close', headers={'X-API-Key': 'manager-token'})
    assert response.status_code == 409, 'closing already closed incident should return 409'
    assert response.json() == {'detail': 'incident already closed'}, 'domain conflict detail is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
