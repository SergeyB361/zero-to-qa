def summarize_plan_findings(lines: list[str]) -> list[str]:
    findings = []
    joined = ' '.join(lines).lower()
    if 'seq scan' in joined:
        findings.append('full scan detected')
    if 'index scan' in joined or 'bitmap index scan' in joined:
        findings.append('index usage detected')
    return findings


def main() -> None:
    sample_plan = ['Seq Scan on tasks', 'Filter: (status = ''open'')']
    assert summarize_plan_findings(sample_plan) == ['full scan detected']
    print('EXPLAIN debugging example passed')


if __name__ == '__main__':
    main()
