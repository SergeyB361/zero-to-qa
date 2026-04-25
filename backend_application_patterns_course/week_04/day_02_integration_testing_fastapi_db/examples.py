from fastapi import Depends, FastAPI, status
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'bap_w4d2_users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)


class UserCreate(BaseModel):
    email: str


engine = create_engine(
    'sqlite+pysqlite:///:memory:',
    future=True,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base.metadata.create_all(engine)
app = FastAPI(title='Backend Patterns Week 4 Day 2')



def get_session():
    with SessionLocal() as session:
        yield session


@app.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, session: Session = Depends(get_session)) -> dict[str, object]:
    user = User(email=payload.email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return {'id': user.id, 'email': user.email}


@app.get('/users')
def list_users(session: Session = Depends(get_session)) -> list[dict[str, object]]:
    rows = session.execute(select(User).order_by(User.id)).scalars().all()
    return [{'id': row.id, 'email': row.email} for row in rows]


if __name__ == '__main__':
    client = TestClient(app)
    print('CREATE ->', client.post('/users', json={'email': 'anna@example.com'}).json())
    print('LIST ->', client.get('/users').json())
