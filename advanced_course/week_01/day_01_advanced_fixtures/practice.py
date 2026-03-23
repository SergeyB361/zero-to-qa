# День 1 — Практика: advanced fixtures

def user_profile() -> dict[str, str]:
    return {'email': 'qa@example.com', 'role': 'user'}


def admin_profile() -> dict[str, str]:
    profile = dict(user_profile())
    profile['role'] = 'admin'
    return profile


def make_ticket(title: str, priority: str) -> dict[str, str]:
    return {'title': title, 'priority': priority}


def resource_log_demo() -> list[str]:
    log: list[str] = []
    log.append('open')
    log.append('inside-test')
    log.append('close')
    return log


def run_checks() -> list[tuple[str, bool]]:
    return [
        ('user email', user_profile()['email'] == 'qa@example.com'),
        ('admin role', admin_profile()['role'] == 'admin'),
        ('factory ticket title', make_ticket('Broken login', 'high')['title'] == 'Broken login'),
        ('yield fixture lifecycle', resource_log_demo() == ['open', 'inside-test', 'close']),
    ]


if __name__ == '__main__':
    print('Отработай composition, factory idea и lifecycle setup/teardown:')
    for name, status in run_checks():
        print(f'{name}: {status}')
