try:
    from hypothesis import given, strategies as st
except ImportError:  # pragma: no cover
    raise SystemExit('Install hypothesis to run this example: pip install hypothesis')


def normalize_email(value: str) -> str:
    return value.strip().lower()


@given(st.text())
def test_normalize_email_is_lowercase(value: str) -> None:
    assert normalize_email(value) == normalize_email(value).lower()


@given(st.lists(st.integers()))
def test_sorted_preserves_length(items: list[int]) -> None:
    assert len(sorted(items)) == len(items)
