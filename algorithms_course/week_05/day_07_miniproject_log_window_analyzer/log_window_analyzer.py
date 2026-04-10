# Неделя 5, День 7 - Мини-проект: Log Window Analyzer

from collections import deque


def push_log(window: deque[str], level: str) -> None:
    # TODO: добавь уровень в окно
    pass


def count_level(window: deque[str], level: str) -> int:
    return -1


def snapshot(window: deque[str]) -> list[str]:
    return []


def main() -> None:
    window = deque(maxlen=4)
    demo_levels = ['INFO', 'ERROR', 'INFO', 'WARN', 'ERROR']

    print('Log Window Analyzer demo scaffold')
    for level in demo_levels:
        push_log(window, level)
        print('window after push:', list(window))

    print('count_level(ERROR) ->', count_level(window, 'ERROR'), '| expected after demo pushes: 2')
    print('snapshot ->', snapshot(window), "| expected after demo pushes: ['ERROR', 'INFO', 'WARN', 'ERROR']")


if __name__ == "__main__":
    main()
