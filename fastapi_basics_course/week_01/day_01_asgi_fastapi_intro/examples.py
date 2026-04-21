from fastapi import FastAPI

app = FastAPI(title='FastAPI Basics Day 1')


@app.get('/')
def read_root() -> dict[str, str]:
    return {'message': 'hello from fastapi basics'}


@app.get('/health')
def healthcheck() -> dict[str, str]:
    return {'status': 'ok'}


if __name__ == '__main__':
    for route in app.routes:
        print(sorted(route.methods or []), route.path)
