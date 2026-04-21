from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, Query, status
from pydantic import BaseModel

app = FastAPI(title='FastAPI Basics Week 2 Day 6')
tasks = [{'id': 1, 'title': 'Write tests', 'status': 'open'}]


class TaskCreate(BaseModel):
    title: str


def get_actor(x_actor: Annotated[str | None, Header()] = None) -> str:
    return x_actor or 'system'


@app.get('/tasks')
def list_tasks(actor: Annotated[str, Depends(get_actor)], limit: int = Query(10, ge=1, le=100)) -> dict[str, object]:
    return {'actor': actor, 'limit': limit, 'items': tasks[:limit]}


@app.post('/tasks', status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> dict[str, object]:
    item = {'id': len(tasks) + 1, 'title': payload.title, 'status': 'open'}
    tasks.append(item)
    return item


@app.get('/tasks/{task_id}')
def get_task(task_id: int) -> dict[str, object]:
    for task in tasks:
        if task['id'] == task_id:
            return task
    raise HTTPException(status_code=404, detail='task not found')
