from unittest.mock import Mock

def send_event(client, payload: dict) -> int:
    response = client.post(payload)
    return response["status"]

def test_send_event() -> None:
    client = Mock()
    client.post.return_value = {"status": 201}
    result = send_event(client, {"name": "login"})
    assert result == 201
    client.post.assert_called_once()
