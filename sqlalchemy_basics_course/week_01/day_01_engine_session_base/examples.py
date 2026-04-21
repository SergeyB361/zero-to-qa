import os

from sqlalchemy import text, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    with Session(engine) as session:
        result = session.execute(text('select 1 as ok')).scalar_one()
        print('Ping ->', result)
        print('Session bind ->', session.bind.dialect.name)
        print('Known tables ->', sorted(Base.metadata.tables.keys()))


if __name__ == '__main__':
    main()
