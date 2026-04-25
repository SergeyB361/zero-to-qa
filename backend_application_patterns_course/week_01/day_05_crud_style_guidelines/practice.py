"""
Практическое задание:
1. Держи CRUD-семантику последовательной.
2. Пусть `POST` возвращает `201` и созданную сущность.
3. Пусть `PATCH` обновляет существующий ресурс.
4. Пусть `DELETE` возвращает `204` без тела.

Например:
- `POST /labels` -> `201`, `{"id": 2, "name": "urgent"}`
- `PATCH /labels/2` -> `200`, `{"id": 2, "name": "critical"}`
- `DELETE /labels/2` -> `204`
- `GET /labels/2` после delete -> `404`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


class LabelCreate(BaseModel):
    name: str


class LabelPatch(BaseModel):
    name: str


class LabelRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'name': 'seed'}]

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def get_by_id(self, label_id: int) -> dict[str, object] | None:
        return next((item for item in self._items if item['id'] == label_id), None)

    def create(self, name: str) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'name': name}
        self._items.append(item)
        return item

    def delete(self, label_id: int) -> None:
        self._items = [item for item in self._items if item['id'] != label_id]


repo = LabelRepository()
app = FastAPI(title='Practice CRUD Style')


@app.get('/labels')
def list_labels() -> list[dict[str, object]]:
    return repo.list_all()


@app.get('/labels/{label_id}')
def get_label(label_id: int) -> dict[str, object]:
    label = repo.get_by_id(label_id)
    if label is None:
        raise HTTPException(status_code=404, detail='label not found')
    return label


@app.post('/labels', status_code=status.HTTP_201_CREATED)
def create_label(payload: LabelCreate) -> dict[str, object]:
    return repo.create(payload.name)


@app.patch('/labels/{label_id}')
def patch_label(label_id: int, payload: LabelPatch) -> dict[str, object]:
    label = repo.get_by_id(label_id)
    if label is None:
        raise HTTPException(status_code=404, detail='label not found')
    # TODO: обновить label['name'] и вернуть обновлённую сущность.
    return {'id': label_id, 'name': 'TODO'}


@app.delete('/labels/{label_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_label(label_id: int) -> Response:
    label = repo.get_by_id(label_id)
    if label is None:
        raise HTTPException(status_code=404, detail='label not found')
    # TODO: удалить label из repository и вернуть 204 без тела.
    return Response(status_code=status.HTTP_200_OK)


def run_checks() -> None:
    client = TestClient(app)

    response = client.post('/labels', json={'name': 'urgent'})
    assert response.status_code == 201, 'create should return 201 Created'
    assert response.json() == {'id': 2, 'name': 'urgent'}, 'created label payload is incorrect'

    response = client.patch('/labels/2', json={'name': 'critical'})
    assert response.status_code == 200, 'patch should return 200 OK'
    assert response.json() == {'id': 2, 'name': 'critical'}, 'patched label payload is incorrect'

    response = client.delete('/labels/2')
    assert response.status_code == 204, 'delete should return 204 No Content'
    assert response.text == '', '204 response should not contain a body'

    response = client.get('/labels/2')
    assert response.status_code == 404, 'deleted label should no longer be available'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
