# Задание 1: detect_seq_scan
# Если в плане есть Seq Scan, верни True.
def detect_seq_scan(lines: list[str]) -> bool:
    return False


# Задание 2: detect_index_usage
# Если в плане есть Index Scan или Bitmap Index Scan, верни True.
def detect_index_usage(lines: list[str]) -> bool:
    return False


# Задание 3: explain_findings_summary
# Верни список коротких выводов по плану.
def explain_findings_summary(lines: list[str]) -> list[str]:
    return []


# Задание 4: write_debugging_workflow
# Верни 4 шага EXPLAIN-debugging workflow.
def write_debugging_workflow() -> list[str]:
    return ['TODO']


# Задание 5: explain_when_to_use_analyze
# Верни 2-3 тезиса, когда нужен EXPLAIN ANALYZE.
def explain_when_to_use_analyze() -> list[str]:
    return ['TODO']


def run_checks() -> None:
    assert isinstance(write_debugging_workflow(), list)
    print('Scaffold checks passed.')


if __name__ == '__main__':
    run_checks()
