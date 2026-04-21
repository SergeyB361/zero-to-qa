from fastapi import APIRouter, FastAPI

app = FastAPI(title='FastAPI Basics Week 2 Day 1')
users_router = APIRouter(prefix='/users', tags=['users'])
projects_router = APIRouter(prefix='/projects', tags=['projects'])


@users_router.get('/')
def list_users() -> list[dict[str, object]]:
    return [{'id': 1, 'name': 'Anna'}]


@projects_router.get('/')
def list_projects() -> list[dict[str, object]]:
    return [{'id': 1, 'name': 'Portal'}]


app.include_router(users_router)
app.include_router(projects_router)
