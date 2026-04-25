"""
Практическое задание:
1. Реализуй integration flow `POST /customers` -> запись в test DB.
2. Реализуй `GET /customers`, который читает реальные строки из БД.
3. Проверь и HTTP-ответ, и фактическое состояние таблицы.

Например:
- `POST /customers` с `{"email": "mila@example.com"}` -> `201`, `{"id": 1, "email": "mila@example.com"}`
- `GET /customers` -> список с этой записью
- direct DB check -> та же строка есть в таблице

Критерий готовности: `run_checks()` проходит без ошибок.
"""

from fastapi import Depends, FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = 'bap_w4d2_customers'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)


class CustomerCreate(BaseModel):
    email: str


engine = create_engine(
    'sqlite+pysqlite:///:memory:',
    future=True,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base.metadata.create_all(engine)
app = FastAPI(title='Backend Patterns Week 4 Day 2 Practice')



def get_session():
    with SessionLocal() as session:
        yield session


@app.post('/customers', status_code=status.HTTP_201_CREATED)
def create_customer(payload: CustomerCreate, session: Session = Depends(get_session)) -> dict[str, object]:
    customer = Customer(email=payload.email)
    session.add(customer)
    # TODO: commit, refresh и вернуть созданный payload.
    return {'id': 0, 'email': 'TODO'}


@app.get('/customers')
def list_customers(session: Session = Depends(get_session)) -> list[dict[str, object]]:
    rows = session.execute(select(Customer).order_by(Customer.id)).scalars().all()
    return [{'id': row.id, 'email': row.email} for row in rows]



def run_checks() -> None:
    client = TestClient(app)

    response = client.post('/customers', json={'email': 'mila@example.com'})
    assert response.status_code == 201, 'create customer route should return 201'
    assert response.json() == {'id': 1, 'email': 'mila@example.com'}, 'created customer payload is incorrect'

    response = client.get('/customers')
    assert response.json() == [{'id': 1, 'email': 'mila@example.com'}], 'list customers payload is incorrect'

    with SessionLocal() as session:
        db_rows = session.execute(select(Customer).order_by(Customer.id)).scalars().all()
        assert [(row.id, row.email) for row in db_rows] == [(1, 'mila@example.com')], 'customer row should be persisted in DB'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
