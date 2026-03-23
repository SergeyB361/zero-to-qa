# День 4 — Практика: property-based testing

def normalize_name(value: str) -> str:
    return value.strip().title()


def describe_abs_properties() -> list[str]:
    return []


def describe_sorted_properties() -> list[str]:
    return []


def describe_bad_fit_cases() -> list[str]:
    return []


def run_checks() -> list[tuple[str, bool]]:
    abs_properties = ' '.join(describe_abs_properties()).lower()
    sorted_properties = ' '.join(describe_sorted_properties()).lower()
    bad_fit_cases = ' '.join(describe_bad_fit_cases()).lower()
    return [
        ('abs mentions non-negative', 'non-negative' in abs_properties or '>= 0' in abs_properties),
        ('abs mentions symmetry', 'abs(-x)' in abs_properties or 'symmetr' in abs_properties),
        ('sorted mentions length', 'length' in sorted_properties or 'длина' in sorted_properties),
        ('sorted mentions order', 'order' in sorted_properties or 'сорт' in sorted_properties),
        ('bad fit contains ui', 'ui' in bad_fit_cases),
        ('bad fit contains expensive env', 'expensive' in bad_fit_cases or 'дорог' in bad_fit_cases),
        ('normalize sample works', normalize_name('  ivan petrov ') == 'Ivan Petrov'),
    ]


if __name__ == '__main__':
    print('Сформулируй свойства как короткие строки:')
    for name, status in run_checks():
        print(f'{name}: {status}')
