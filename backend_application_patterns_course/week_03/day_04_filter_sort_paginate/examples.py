from fastapi import FastAPI, Query
from fastapi.testclient import TestClient


ITEMS = [
    {'id': 1, 'title': 'login bug', 'status': 'open', 'priority': 3},
    {'id': 2, 'title': 'profile typo', 'status': 'closed', 'priority': 1},
    {'id': 3, 'title': 'invoice bug', 'status': 'open', 'priority': 2},
    {'id': 4, 'title': 'slow dashboard', 'status': 'open', 'priority': 5},
]



def list_items(status: str | None, sort_by: str, page: int, page_size: int) -> dict[str, object]:
    rows = [item for item in ITEMS if status is None or item['status'] == status]

    if sort_by == 'priority_desc':
        rows = sorted(rows, key=lambda item: item['priority'], reverse=True)
    elif sort_by == 'id_asc':
        rows = sorted(rows, key=lambda item: item['id'])

    total = len(rows)
    start = (page - 1) * page_size
    end = start + page_size
    return {'items': rows[start:end], 'total': total, 'page': page, 'page_size': page_size}


app = FastAPI(title='Backend Patterns Week 3 Day 4')


@app.get('/items')
def get_items(
    status: str | None = Query(default=None),
    sort_by: str = Query(default='id_asc'),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=2, ge=1, le=50),
) -> dict[str, object]:
    return list_items(status=status, sort_by=sort_by, page=page, page_size=page_size)


if __name__ == '__main__':
    client = TestClient(app)
    print('OPEN + PRIORITY ->', client.get('/items?status=open&sort_by=priority_desc&page=1&page_size=2').json())
    print('SECOND PAGE ->', client.get('/items?page=2&page_size=2').json())
