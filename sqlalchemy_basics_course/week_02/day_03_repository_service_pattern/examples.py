import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class ApiClient(Base):
    __tablename__ = 'sa_w2d3_api_clients'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)
    is_active: Mapped[bool]


class ApiClientRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_name(self, name: str) -> ApiClient | None:
        return self.session.execute(select(ApiClient).where(ApiClient.name == name)).scalar_one_or_none()

    def create(self, name: str) -> ApiClient:
        item = ApiClient(name=name, is_active=True)
        self.session.add(item)
        return item


class ApiClientService:
    def __init__(self, repo: ApiClientRepository) -> None:
        self.repo = repo

    def ensure_client(self, name: str) -> dict[str, object]:
        existing = self.repo.get_by_name(name)
        if existing is not None:
            return {'id': existing.id, 'name': existing.name, 'created': False}
        created = self.repo.create(name)
        return {'id': created.id, 'name': created.name, 'created': True}


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        service = ApiClientService(ApiClientRepository(session))
        first = service.ensure_client('billing-bot')
        session.commit()
        second = service.ensure_client('billing-bot')
        print('First ->', first)
        print('Second ->', second)


if __name__ == '__main__':
    main()
