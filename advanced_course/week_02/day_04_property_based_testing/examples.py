try:
    from hypothesis import given, strategies as st
except ImportError:  # pragma: no cover
    raise SystemExit("Install hypothesis to run this example: pip install hypothesis")


def normalize_email(value: str) -> str:
    return value.strip().lower()


@given(st.text())
def test_normalize_email_is_lowercase(value: str) -> None:
    assert normalize_email(value) == normalize_email(value).lower()
