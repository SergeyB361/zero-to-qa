from fastapi import FastAPI

app = FastAPI(title='FastAPI Basics Day 2')
items = [{'id': 1, 'name': 'notebook'}, {'id': 2, 'name': 'mouse'}]


@app.get('/items')
def list_items() -> list[dict[str, object]]:
    return items


@app.get('/items/{item_id}')
def get_item(item_id: int) -> dict[str, object]:
    return next(item for item in items if item['id'] == item_id)


@app.post('/items')
def create_item() -> dict[str, str]:
    return {'detail': 'creation example'}


@app.delete('/items/{item_id}')
def delete_item(item_id: int) -> dict[str, object]:
    return {'deleted_id': item_id}


if __name__ == '__main__':
    for route in app.routes:
        print(sorted(route.methods or []), route.path)
