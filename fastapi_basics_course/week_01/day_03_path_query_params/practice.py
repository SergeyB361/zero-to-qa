"""
Практическое задание:
1. Верни path parameter из detail endpoint без искажения.
2. Отрази query params в list endpoint корректно и с нужными типами.
3. Собери route, где одновременно участвуют path и query параметры.

Например:
- `GET /products/7` -> `{"product_id": 7, "detail": "full product view"}`
- `GET /products?category=qa&limit=5&active_only=false` -> `{"category": "qa", "limit": 5, "active_only": false}`
- `GET /reports/2026/4?team=api` -> `{"year": 2026, "month": 4, "team": "api"}`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI(title='Practice Day 3')


@app.get('/products/{product_id}')
def get_product(product_id: int) -> dict[str, object]:
    return {'product_id': product_id, 'detail': 'TODO'}


@app.get('/products')
def list_products(category: str | None = None, limit: int = 20, active_only: bool = True) -> dict[str, object]:
    return {'category': category, 'limit': limit, 'active_only': active_only}


@app.get('/reports/{year}/{month}')
def monthly_report(year: int, month: int, team: str | None = None) -> dict[str, object]:
    return {'year': year, 'month': month, 'team': team}


client = TestClient(app)


def run_checks() -> None:
    response = client.get('/products/7')
    assert response.status_code == 200, 'expected 200 OK response'
    body = response.json()
    assert body['product_id'] == 7, 'path parameter should be returned unchanged'
    assert body['detail'] != 'TODO', 'detail marker is still TODO'

    response = client.get('/products?category=qa&limit=5&active_only=false')
    assert response.status_code == 200, 'expected 200 OK response'
    body = response.json()
    assert body == {'category': 'qa', 'limit': 5, 'active_only': False}, 'query params should be parsed and reflected correctly'

    response = client.get('/reports/2026/4?team=api')
    assert response.status_code == 200, 'expected 200 OK response'
    assert response.json() == {'year': 2026, 'month': 4, 'team': 'api'}, 'path/query combination is not returned correctly'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
