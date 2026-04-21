from typing import Annotated

from fastapi import Depends, FastAPI, Header, Query
from fastapi.testclient import TestClient

app = FastAPI(title='FastAPI Basics Day 6')


def get_request_source(x_request_source: Annotated[str | None, Header()] = None) -> str:
    return x_request_source or 'unknown'


@app.get('/search')
def search_items(source: Annotated[str, Depends(get_request_source)], limit: int = Query(default=10, ge=1, le=100)) -> dict[str, object]:
    return {'source': source, 'limit': limit}


if __name__ == '__main__':
    client = TestClient(app)
    print('GET /search ->', client.get('/search').json())
    print('GET /search?limit=5 with header ->', client.get('/search?limit=5', headers={'x-request-source': 'qa-ui'}).json())
