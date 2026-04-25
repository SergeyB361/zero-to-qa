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
        if incident['status'] == 'closed':
            raise IncidentAlreadyClosedError('incident already closed')
        incident['status'] = 'closed'
        return incident


app = FastAPI(title='Backend Patterns Week 3 Day 6')
service = IncidentService()


@app.patch('/incidents/{incident_id}/close')
def close_incident(incident_id: int, _: ActorContext = Depends(require_manager)) -> dict[str, object]:
    try:
        return service.close_incident(incident_id)
    except IncidentAlreadyClosedError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


if __name__ == '__main__':
    client = TestClient(app)
    print('VIEWER ->', client.patch('/incidents/1/close', headers={'X-API-Key': 'viewer-token'}).status_code)
    print('MANAGER ->', client.patch('/incidents/1/close', headers={'X-API-Key': 'manager-token'}).json())
    print('SECOND CLOSE ->', client.patch('/incidents/1/close', headers={'X-API-Key': 'manager-token'}).status_code)
