from fastapi import FastAPI, status
from fastapi.testclient import TestClient

app = FastAPI(title='FastAPI Basics Week 2 Day 3')


@app.get('/ping')
def ping() -> dict[str, str]:
    return {'status': 'pong'}


@app.post('/echo', status_code=status.HTTP_201_CREATED)
def echo() -> dict[str, str]:
    return {'detail': 'created'}


client = TestClient(app)


def run_demo_checks() -> None:
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'status': 'pong'}

    response = client.post('/echo')
    assert response.status_code == 201
    assert response.json()['detail'] == 'created'


if __name__ == '__main__':
    run_demo_checks()
    print('TestClient demo checks passed')
