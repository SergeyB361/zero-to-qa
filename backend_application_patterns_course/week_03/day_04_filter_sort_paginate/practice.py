"""
Практическое задание:
1. Реализуй list endpoint c `status`, `sort_by`, `page`, `page_size`.
2. Применяй операции в правильном порядке: filter -> sort -> paginate.
3. Верни `items`, `total`, `page`, `page_size`.

Например:
- `GET /orders?status=new&sort_by=amount_desc&page=1&page_size=2`
- ответ -> только `new` orders, отсортированные по amount, первая страница, плюс metadata

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import FastAPI, Query
from fastapi.testclient import TestClient


ORDERS = [
    {'id': 1, 'title': 'web portal', 'status': 'new', 'amount': 300},
    {'id': 2, 'title': 'mobile app', 'status': 'paid', 'amount': 150},
    {'id': 3, 'title': 'public api', 'status': 'new', 'amount': 220},
    {'id': 4, 'title': 'internal tool', 'status': 'new', 'amount': 90},
]



def list_orders(status: str | None, sort_by: str, page: int, page_size: int) -> dict[str, object]:
    # TODO: filter -> sort -> paginate и вернуть metadata.
    return {'items': [], 'total': 0, 'page': page, 'page_size': page_size}


app = FastAPI(title='Backend Patterns Week 3 Day 4 Practice')


@app.get('/orders')
def get_orders(
    status: str | None = Query(default=None),
    sort_by: str = Query(default='id_asc'),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=2, ge=1, le=50),
) -> dict[str, object]:
    return list_orders(status=status, sort_by=sort_by, page=page, page_size=page_size)



def run_checks() -> None:
    client = TestClient(app)

    response = client.get('/orders?status=new&sort_by=amount_desc&page=1&page_size=2')
    assert response.status_code == 200, 'list orders route should return 200'
    assert response.json() == {
        'items': [
            {'id': 1, 'title': 'web portal', 'status': 'new', 'amount': 300},
            {'id': 3, 'title': 'public api', 'status': 'new', 'amount': 220},
        ],
        'total': 3,
        'page': 1,
        'page_size': 2,
    }, 'filtered/sorted first page is incorrect'

    response = client.get('/orders?sort_by=id_asc&page=2&page_size=2')
    assert response.json() == {
        'items': [
            {'id': 3, 'title': 'public api', 'status': 'new', 'amount': 220},
            {'id': 4, 'title': 'internal tool', 'status': 'new', 'amount': 90},
        ],
        'total': 4,
        'page': 2,
        'page_size': 2,
    }, 'second page payload is incorrect'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
