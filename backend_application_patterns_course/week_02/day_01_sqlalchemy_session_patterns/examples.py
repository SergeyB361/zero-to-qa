from sqlalchemy import String, UniqueConstraint, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


class Base(DeclarativeBase):
    pass


class Member(Base):
    __tablename__ = 'bap_w2d1_members'
    __table_args__ = (UniqueConstraint('email', name='uq_member_email'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120))


engine = create_engine(
    'sqlite+pysqlite:///:memory:',
    future=True,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base.metadata.create_all(engine)


class MemberService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def register(self, name: str, email: str) -> dict[str, object]:
        member = Member(name=name, email=email)
        self.session.add(member)
        self.session.commit()
        self.session.refresh(member)
        return {'id': member.id, 'name': member.name, 'email': member.email}


if __name__ == '__main__':
    with SessionLocal() as session:
        service = MemberService(session)
        print('REGISTER ->', service.register('Anna', 'anna@example.com'))
        try:
            service.register('Anna 2', 'anna@example.com')
        except IntegrityError:
            session.rollback()
            print('ROLLBACK -> duplicate email rejected')

    with SessionLocal() as session:
        rows = session.execute(select(Member).order_by(Member.id)).scalars().all()
        print('MEMBERS ->', [{'id': row.id, 'email': row.email} for row in rows])
