from fastapi import FastAPI, HTTPException, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


class ProfileCreate(BaseModel):
    nickname: str


class ProfilePatch(BaseModel):
    nickname: str


class ProfileRepository:
    def __init__(self) -> None:
        self._items = [{'id': 1, 'nickname': 'seed'}]

    def list_all(self) -> list[dict[str, object]]:
        return list(self._items)

    def get_by_id(self, profile_id: int) -> dict[str, object] | None:
        return next((item for item in self._items if item['id'] == profile_id), None)

    def create(self, nickname: str) -> dict[str, object]:
        item = {'id': len(self._items) + 1, 'nickname': nickname}
        self._items.append(item)
        return item


repo = ProfileRepository()
app = FastAPI(title='CRUD Style Example')


@app.get('/profiles')
def list_profiles() -> list[dict[str, object]]:
    return repo.list_all()


@app.get('/profiles/{profile_id}')
def get_profile(profile_id: int) -> dict[str, object]:
    profile = repo.get_by_id(profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail='profile not found')
    return profile


@app.post('/profiles', status_code=status.HTTP_201_CREATED)
def create_profile(payload: ProfileCreate) -> dict[str, object]:
    return repo.create(payload.nickname)


@app.patch('/profiles/{profile_id}')
def patch_profile(profile_id: int, payload: ProfilePatch) -> dict[str, object]:
    profile = repo.get_by_id(profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail='profile not found')
    profile['nickname'] = payload.nickname
    return profile


@app.delete('/profiles/{profile_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(profile_id: int) -> Response:
    profile = repo.get_by_id(profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail='profile not found')
    repo._items = [item for item in repo._items if item['id'] != profile_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)


if __name__ == '__main__':
    client = TestClient(app)
    print('POST /profiles ->', client.post('/profiles', json={'nickname': 'qa'}).status_code)
    print('PATCH /profiles/1 ->', client.patch('/profiles/1', json={'nickname': 'lead'}).json())
    print('DELETE /profiles/1 ->', client.delete('/profiles/1').status_code)
