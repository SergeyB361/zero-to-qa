from contextlib import asynccontextmanager
from time import perf_counter

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.service_name = 'fastapi-basics-demo'
    yield


app = FastAPI(title='FastAPI Basics Week 2 Day 5', lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:3000'], allow_methods=['*'], allow_headers=['*'])


@app.middleware('http')
async def timing_middleware(request: Request, call_next):
    started = perf_counter()
    response = await call_next(request)
    response.headers['X-Process-Time'] = f'{perf_counter() - started:.6f}'
    return response


@app.get('/info')
def info() -> dict[str, str]:
    return {'service': app.state.service_name}


if __name__ == '__main__':
    with TestClient(app) as client:
        response = client.get('/info', headers={'Origin': 'http://localhost:3000'})
        print('GET /info ->', response.status_code, response.json())
        print('X-Process-Time ->', response.headers.get('x-process-time'))
        print('Access-Control-Allow-Origin ->', response.headers.get('access-control-allow-origin'))
