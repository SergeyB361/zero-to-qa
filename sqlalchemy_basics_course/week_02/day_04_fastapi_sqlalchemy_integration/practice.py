"""
Практическое задание:
1. Подключи `Session` через FastAPI dependency.
2. Реализуй list/create для `ServiceAccount`.
3. После `POST` новый аккаунт должен появляться в повторном `GET`.

Например:
- `POST /service-accounts` -> `201` и `{'id': 1, 'name': 'worker-bot'}`
- `GET /service-accounts` -> `[{'id': 1, 'name': 'worker-bot'}]`

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import os
from typing import Annotated

from fastapi import Depends, FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class ServiceAccount(Base):
    __tablename__ = 'sa_w2d4_service_accounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)


class ServiceAccountCreate(BaseModel):
    name: str


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
app = FastAPI(title='Practice SQLAlchemy + FastAPI')


def get_session():
    with SessionLocal() as session:
        yield session


@app.get('/service-accounts')
def list_service_accounts(session: Annotated[Session, Depends(get_session)]) -> list[dict[str, object]]:
    # TODO: прочитай rows через ORM и верни их как JSON-friendly list.
    return []


@app.post('/service-accounts', status_code=status.HTTP_201_CREATED)
def create_service_account(payload: ServiceAccountCreate, session: Annotated[Session, Depends(get_session)]) -> dict[str, object]:
    # TODO: создай account через session и сделай commit.
    return {'id': 0, 'name': 'TODO'}


client = TestClient(app)


def run_checks() -> None:
    created = client.post('/service-accounts', json={'name': 'worker-bot'})
    assert created.status_code == 201, 'POST /service-accounts should return 201 Created'
    assert created.json()['name'] == 'worker-bot', 'created account should echo request name'

    listed = client.get('/service-accounts')
    assert listed.status_code == 200, 'GET /service-accounts should return 200 OK'
    assert listed.json() == [{'id': 1, 'name': 'worker-bot'}], 'new account should be visible in subsequent list call'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
