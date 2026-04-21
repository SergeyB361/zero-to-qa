from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title='Notes API')
notes = [{'id': 1, 'title': 'Intro', 'content': 'FastAPI basics', 'is_archived': False}]


class NoteCreate(BaseModel):
    title: str
    content: str
    is_archived: bool = False


class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    is_archived: bool


@app.get('/notes', response_model=list[NoteOut])
def list_notes() -> list[NoteOut]:
    return [NoteOut(**note) for note in notes]


@app.get('/notes/{note_id}', response_model=NoteOut)
def get_note(note_id: int) -> NoteOut:
    for note in notes:
        if note['id'] == note_id:
            return NoteOut(**note)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='note not found')


@app.post('/notes', response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate) -> NoteOut:
    new_note = {'id': len(notes) + 1, **payload.model_dump()}
    notes.append(new_note)
    return NoteOut(**new_note)


@app.delete('/notes/{note_id}')
def delete_note(note_id: int) -> dict[str, object]:
    for index, note in enumerate(notes):
        if note['id'] == note_id:
            deleted = notes.pop(index)
            return {'deleted_id': deleted['id']}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='note not found')


client = TestClient(app)


def run_smoke_checks() -> None:
    response = client.get('/notes')
    assert response.status_code == 200, 'expected 200 OK response'
    assert isinstance(response.json(), list), 'endpoint should return a JSON list'

    response = client.get('/notes/1')
    assert response.status_code == 200, 'expected 200 OK response'

    response = client.post('/notes', json={'title': 'Guide', 'content': 'FastAPI docs', 'is_archived': False})
    assert response.status_code == 201, 'expected 201 Created response'
    assert response.json()['title'] == 'Guide', 'POST /notes should create Guide note'

    response = client.delete('/notes/1')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json()['deleted_id'] == 1, 'DELETE /notes/1 should return deleted_id=1'


if __name__ == '__main__':
    try:
        run_smoke_checks()
    except AssertionError as exc:
        print(f'Smoke check failed: {exc}')
        raise
    print('Notes API smoke checks passed')
