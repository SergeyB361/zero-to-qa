from dataclasses import dataclass

from sqlalchemy import String, UniqueConstraint, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool


@dataclass(slots=True)
class AppSettings:
    database_url: str = 'sqlite+pysqlite:///:memory:'


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = 'bap_w2d6_customers'
    __table_args__ = (UniqueConstraint('email', name='uq_customer_email'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120))


class DuplicateCustomerEmailError(RuntimeError):
    pass


class CustomerRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, name: str, email: str) -> Customer:
        customer = Customer(name=name, email=email)
        self.session.add(customer)
        return customer

    def list_all(self) -> list[dict[str, object]]:
        rows = self.session.execute(select(Customer).order_by(Customer.id)).scalars().all()
        return [{'id': row.id, 'name': row.name, 'email': row.email} for row in rows]


class CustomerService:
    def __init__(self, repo: CustomerRepository, session: Session) -> None:
        self.repo = repo
        self.session = session

    def register_customer(self, name: str, email: str) -> dict[str, object]:
        customer = self.repo.create(name, email)
        try:
            self.session.commit()
        except IntegrityError as exc:
            self.session.rollback()
            raise DuplicateCustomerEmailError('customer email already exists') from exc
        self.session.refresh(customer)
        return {'id': customer.id, 'name': customer.name, 'email': customer.email}



def build_session_factory(settings: AppSettings) -> sessionmaker[Session]:
    engine = create_engine(
        settings.database_url,
        future=True,
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine, expire_on_commit=False, future=True)


if __name__ == '__main__':
    SessionLocal = build_session_factory(AppSettings())
    with SessionLocal() as session:
        service = CustomerService(CustomerRepository(session), session)
        print('REGISTER ->', service.register_customer('Anna', 'anna@example.com'))
        try:
            service.register_customer('Anna 2', 'anna@example.com')
        except DuplicateCustomerEmailError as exc:
            print('DUPLICATE ->', str(exc))
        print('CUSTOMERS ->', CustomerRepository(session).list_all())
