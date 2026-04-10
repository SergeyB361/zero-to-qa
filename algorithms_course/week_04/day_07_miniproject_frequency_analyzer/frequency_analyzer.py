# Неделя 4, День 7 - Мини-проект: Frequency Analyzer


def build_frequency_map(items: list[str]) -> dict[str, int]:
    return {}


def count_unique(items: list[str]) -> int:
    return -1


def most_frequent(items: list[str]) -> str:
    return ''


def items_with_frequency_one(items: list[str]) -> list[str]:
    return []


def main() -> None:
    sample = ['api', 'db', 'api', 'ui', 'db', 'api', 'log']

    print('Frequency Analyzer demo scaffold')
    print('build_frequency_map ->', build_frequency_map(sample), "| expected: {'api': 3, 'db': 2, 'ui': 1, 'log': 1}")
    print('count_unique ->', count_unique(sample), '| expected: 4')
    print('most_frequent ->', most_frequent(sample), "| expected: 'api'")
    print('items_with_frequency_one ->', items_with_frequency_one(sample), "| expected: ['ui', 'log']")


if __name__ == "__main__":
    main()
