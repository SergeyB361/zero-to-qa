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


class Team(Base):
    __tablename__ = 'sa_w2d4_teams'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)


class TeamCreate(BaseModel):
    name: str


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
app = FastAPI(title='SQLAlchemy + FastAPI example')


def get_session():
    with SessionLocal() as session:
        yield session


@app.get('/teams')
def list_teams(session: Annotated[Session, Depends(get_session)]) -> list[dict[str, object]]:
    rows = session.execute(select(Team).order_by(Team.name)).scalars().all()
    return [{'id': row.id, 'name': row.name} for row in rows]


@app.post('/teams', status_code=status.HTTP_201_CREATED)
def create_team(payload: TeamCreate, session: Annotated[Session, Depends(get_session)]) -> dict[str, object]:
    team = Team(name=payload.name)
    session.add(team)
    session.commit()
    return {'id': team.id, 'name': team.name}


if __name__ == '__main__':
    client = TestClient(app)
    created = client.post('/teams', json={'name': 'backend'})
    print('POST /teams ->', created.status_code, created.json())
    print('GET /teams ->', client.get('/teams').json())
