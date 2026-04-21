from fastapi import FastAPI

app = FastAPI(title='FastAPI Basics Day 3')


@app.get('/users/{user_id}')
def get_user(user_id: int) -> dict[str, int]:
    return {'user_id': user_id}


@app.get('/users')
def list_users(team: str | None = None, limit: int = 10) -> dict[str, object]:
    return {'team': team, 'limit': limit}


@app.get('/reports/{year}/{month}')
def report(year: int, month: int, verbose: bool = False) -> dict[str, object]:
    return {'year': year, 'month': month, 'verbose': verbose}
