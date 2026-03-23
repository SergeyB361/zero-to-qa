import pytest

@pytest.fixture(scope="module")
def api_base_url() -> str:
    return "https://reqres.in/api"

def test_base_url(api_base_url: str) -> None:
    assert api_base_url.startswith("https://")
