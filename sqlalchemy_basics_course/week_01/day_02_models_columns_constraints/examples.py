import os

from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class OrmUser(Base):
    __tablename__ = 'sa_day2_users'

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(50), unique=True)
    team: Mapped[str] = mapped_column(String(30))


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(OrmUser(login='anna', team='web'))
        session.commit()
        row = session.query(OrmUser).filter_by(login='anna').one()
        print('Created ->', {'id': row.id, 'login': row.login, 'team': row.team})


if __name__ == '__main__':
    main()
