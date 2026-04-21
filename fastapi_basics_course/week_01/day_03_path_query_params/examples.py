from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI(title='FastAPI Basics Day 3')


@app.get('/users/{user_id}')
def get_user(user_id: int) -> dict[str, int]:
    return {'user_id': user_id}


@app.get('/users')
def list_users(team: str | None = None, limit: int = 10) -> dict[str, object]:
    return {'team': team, 'limit': limit}


@app.get('/reports/{year}/{month}')
def report(year: int, month: int, verbose: bool = False) -> dict[str, object]:
    return {'year': year, 'month': month, 'verbose': verbose}


if __name__ == '__main__':
    client = TestClient(app)
    print('GET /users/42 ->', client.get('/users/42').json())
    print('GET /users?team=qa&limit=5 ->', client.get('/users?team=qa&limit=5').json())
    print('GET /reports/2026/4?verbose=true ->', client.get('/reports/2026/4?verbose=true').json())
