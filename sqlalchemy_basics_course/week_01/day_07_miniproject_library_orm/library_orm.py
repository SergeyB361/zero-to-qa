import os

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg://postgres:postgres@localhost:5432/zero_to_qa')


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = 'sa_library_authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)
    books: Mapped[list['Book']] = relationship(back_populates='author')


class Book(Base):
    __tablename__ = 'sa_library_books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    author_id: Mapped[int] = mapped_column(ForeignKey('sa_library_authors.id'))
    author: Mapped[Author] = relationship(back_populates='books')


def seed_library(session: Session) -> None:
    # TODO: создай автора и пару книг через ORM.
    pass


def list_books_with_authors(session: Session) -> list[dict[str, str]]:
    # TODO: верни список книг с именем автора.
    return []


def create_book(session: Session, author_name: str, title: str) -> dict[str, str]:
    # TODO: добавь новую книгу существующему или новому автору.
    return {'author': 'TODO', 'title': 'TODO'}


def run_smoke_checks() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        seed_library(session)
        seeded = list_books_with_authors(session)
        assert len(seeded) >= 2, 'seed_library should create at least two books'
        created = create_book(session, 'Anna', 'SQLAlchemy Patterns')
        assert created == {'author': 'Anna', 'title': 'SQLAlchemy Patterns'}, 'create_book should return created author/title pair'
        session.commit()
        items = list_books_with_authors(session)
        assert any(item['title'] == 'SQLAlchemy Patterns' for item in items), 'newly created book should appear in listing'


if __name__ == '__main__':
    try:
        run_smoke_checks()
    except AssertionError as exc:
        print(f'Smoke check failed: {exc}')
        raise
    print('Library ORM smoke checks passed')
