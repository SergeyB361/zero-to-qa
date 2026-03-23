from unittest.mock import Mock

# День 4 — Практика: mocking deeper

def send_welcome(email: str, mailer: Mock) -> None:
    mailer.send(email, template='welcome')


def send_bulk(emails: list[str], mailer: Mock) -> None:
    for email in emails:
        mailer.send(email, template='bulk')


def run_checks() -> list[tuple[str, bool]]:
    mailer = Mock()
    send_welcome('qa@example.com', mailer)
    send_bulk(['a@example.com', 'b@example.com'], mailer)
    return [
        ('welcome call recorded', mailer.send.call_args_list[0].args[0] == 'qa@example.com'),
        ('welcome template kept', mailer.send.call_args_list[0].kwargs == {'template': 'welcome'}),
        ('bulk call count', mailer.send.call_count == 3),
    ]


if __name__ == '__main__':
    print('Потренируйся читать call_args и считать вызовы mock:')
    for name, status in run_checks():
        print(f'{name}: {status}')
