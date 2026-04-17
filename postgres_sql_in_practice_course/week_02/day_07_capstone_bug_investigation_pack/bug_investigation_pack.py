from __future__ import annotations


def collect_context() -> dict:
    raise NotImplementedError


# core queries should return a compact investigation snapshot
def run_core_queries() -> list[dict]:
    raise NotImplementedError


# summarize findings for another engineer
def summarize_findings(rows: list[dict]) -> list[str]:
    raise NotImplementedError


def main() -> None:
    print('Bug investigation pack scaffold')
    print('Implement collect_context, run_core_queries, summarize_findings')


if __name__ == '__main__':
    main()
