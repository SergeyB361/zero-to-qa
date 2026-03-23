# День 1 — Практика: factories

DEFAULT_EMAIL = 'qa@example.com'
DEFAULT_ROLE = 'user'
DEFAULT_PRIORITY = 'medium'


def make_user(email: str = DEFAULT_EMAIL, role: str = DEFAULT_ROLE, active: bool = True) -> dict[str, object]:
    return {
        'email': email,
        'role': role,
        'active': active,
    }


def make_order(total: int = 100, status: str = 'new') -> dict[str, object]:
    # Добавь currency='RUB' и customer_type='regular'.
    return {
        'total': total,
        'status': status,
        'currency': '',
        'customer_type': '',
    }


def make_ticket(title: str, priority: str = DEFAULT_PRIORITY) -> dict[str, str]:
    # Добавь поле owner со значением 'qa-team'.
    return {
        'title': title,
        'priority': priority,
        'owner': '',
    }


def run_checks() -> list[tuple[str, bool]]:
    default_user = make_user()
    custom_order = make_order(total=250, status='paid')
    incident = make_ticket('Login is broken', priority='high')
    return [
        ('user email default', default_user['email'] == DEFAULT_EMAIL),
        ('order currency set', custom_order['currency'] == 'RUB'),
        ('order customer type set', custom_order['customer_type'] == 'regular'),
        ('ticket owner set', incident['owner'] == 'qa-team'),
        ('ticket priority kept', incident['priority'] == 'high'),
    ]


if __name__ == '__main__':
    print('Сделай factories и проверь результаты:')
    for name, status in run_checks():
        print(f'{name}: {status}')
