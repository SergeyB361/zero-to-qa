from unittest.mock import Mock


def send_welcome(email: str, mailer) -> None:
    mailer.send(email, template="welcome")


def get_user_name(client, user_id: int) -> str:
    response = client.fetch_user(user_id)
    return response["name"]


def test_send_welcome_calls_mailer() -> None:
    mailer = Mock()
    send_welcome("qa@example.com", mailer)
    mailer.send.assert_called_once_with("qa@example.com", template="welcome")


def test_side_effect_timeout() -> None:
    client = Mock()
    client.fetch_user.side_effect = TimeoutError("gateway timeout")

    try:
        get_user_name(client, 10)
    except TimeoutError as exc:
        assert str(exc) == "gateway timeout"
    else:
        raise AssertionError("TimeoutError was expected")
