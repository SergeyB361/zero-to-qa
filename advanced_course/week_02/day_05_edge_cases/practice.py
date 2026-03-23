# День 5 — Практика: edge cases

def age_edges() -> list[int]:
    return []


def username_edges() -> list[str]:
    return []


def amount_edges() -> list[int]:
    return []


def run_checks() -> list[tuple[str, bool]]:
    ages = age_edges()
    names = username_edges()
    amounts = amount_edges()
    return [
        ('age lower boundary covered', {17, 18, 19}.issubset(set(ages))),
        ('age upper boundary covered', {64, 65, 66}.issubset(set(ages))),
        ('username includes empty or too short', any(len(name) < 3 for name in names)),
        ('username includes max length', any(len(name) == 20 for name in names)),
        ('amount includes zero', 0 in amounts),
        ('amount includes valid max', 10_000 in amounts),
        ('amount includes invalid above max', 10_001 in amounts),
    ]


if __name__ == '__main__':
    print('Собери compact edge наборы:')
    for name, status in run_checks():
        print(f'{name}: {status}')
