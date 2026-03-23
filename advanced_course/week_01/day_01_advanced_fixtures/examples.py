import pytest


@pytest.fixture
def user_data() -> dict[str, str]:
    return {"email": "user@example.com", "role": "user"}


@pytest.fixture
def admin_user(user_data: dict[str, str]) -> dict[str, str]:
    data = user_data.copy()
    data["role"] = "admin"
    return data


@pytest.fixture
def make_user():
    def _make_user(email: str, role: str = "user") -> dict[str, str]:
        return {"email": email, "role": role}

    return _make_user


@pytest.fixture
def event_log() -> list[str]:
    log: list[str] = []
    log.append("setup")
    yield log
    log.append("teardown")


def test_admin_fixture(admin_user: dict[str, str]) -> None:
    assert admin_user["role"] == "admin"


def test_factory_fixture(make_user) -> None:
    guest = make_user("guest@example.com", role="guest")
    assert guest == {"email": "guest@example.com", "role": "guest"}


def test_yield_fixture(event_log: list[str]) -> None:
    assert event_log == ["setup"]
