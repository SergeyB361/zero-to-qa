from unittest.mock import patch

def get_settings() -> dict:
    return {"env": "prod"}

def load_env_name() -> str:
    return get_settings()["env"]

@patch(__name__ + ".get_settings")
def test_load_env_name(mock_get_settings) -> None:
    mock_get_settings.return_value = {"env": "test"}
    assert load_env_name() == "test"
