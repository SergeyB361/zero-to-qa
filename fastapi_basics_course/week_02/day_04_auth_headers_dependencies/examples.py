from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.testclient import TestClient

app = FastAPI(title='FastAPI Basics Week 2 Day 4')


def verify_token(x_api_key: Annotated[str | None, Header()] = None) -> str:
    if x_api_key != 'demo-secret':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid api key')
    return x_api_key


@app.get('/protected')
def protected_route(api_key: Annotated[str, Depends(verify_token)]) -> dict[str, str]:
    return {'auth': 'passed', 'token': api_key}


if __name__ == '__main__':
    client = TestClient(app)
    bad = client.get('/protected')
    print('GET /protected without token ->', bad.status_code, bad.json())
    good = client.get('/protected', headers={'x-api-key': 'demo-secret'})
    print('GET /protected with token ->', good.status_code, good.json())
