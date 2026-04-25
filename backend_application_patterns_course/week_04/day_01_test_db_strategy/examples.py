from sqlalchemy import String, create_engine, delete, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'bap_w4d1_users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)


engine = create_engine(
    'sqlite+pysqlite:///:memory:',
    future=True,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base.metadata.create_all(engine)



def reset_database(session: Session) -> None:
    session.execute(delete(User))
    session.commit()



def seed_users(session: Session, emails: list[str]) -> None:
    session.add_all([User(email=email) for email in emails])
    session.commit()



def list_emails(session: Session) -> list[str]:
    return session.execute(select(User.email).order_by(User.id)).scalars().all()


if __name__ == '__main__':
    with SessionLocal() as session:
        seed_users(session, ['anna@example.com', 'boris@example.com'])
        print('FIRST TEST DATA ->', list_emails(session))

        reset_database(session)
        seed_users(session, ['mila@example.com'])
        print('SECOND TEST DATA ->', list_emails(session))
        print('MEANING -> each scenario gets its own clean data state')
