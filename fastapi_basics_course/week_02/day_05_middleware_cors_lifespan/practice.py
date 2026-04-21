"""
Практическое задание:
1. Используй lifespan для инициализации app state.
2. Добавь middleware, который пишет timing header.
3. Настрой CORS так, чтобы нужный origin получал allow-origin header.

Например:
- `GET /mode` -> `{"mode": "practice"}`
- в response headers должен быть `X-Process-Time`
- при `Origin: http://localhost:5173` должен появиться `Access-Control-Allow-Origin: http://localhost:5173`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from contextlib import asynccontextmanager
from time import perf_counter

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.mode = 'practice'
    yield


app = FastAPI(title='Practice Week 2 Day 5', lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.middleware('http')
async def timing_middleware(request: Request, call_next):
    started = perf_counter()
    response = await call_next(request)
    response.headers['X-Process-Time'] = f'{perf_counter() - started:.6f}'
    return response


@app.get('/mode')
def mode() -> dict[str, str]:
    return {'mode': app.state.mode}


def run_checks() -> None:
    with TestClient(app) as client:
        response = client.get('/mode', headers={'Origin': 'http://localhost:5173'})
        assert response.status_code == 200, 'expected 200 OK response'
        assert response.json() == {'mode': 'practice'}, 'lifespan state was not initialized correctly'
        assert 'x-process-time' in response.headers, 'middleware did not add timing header'
        assert response.headers['access-control-allow-origin'] == 'http://localhost:5173', 'CORS header is not configured as expected'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
