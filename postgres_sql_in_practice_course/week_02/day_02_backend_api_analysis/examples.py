def summarize_endpoint_metrics(rows: list[dict]) -> list[str]:
    return [f"{row['endpoint']} -> {row['avg_latency_ms']}ms" for row in rows]


def main() -> None:
    rows = [{'endpoint': '/orders', 'avg_latency_ms': 250}]
    assert summarize_endpoint_metrics(rows) == ['/orders -> 250ms']
    print('Backend/API analysis example passed')


if __name__ == '__main__':
    main()
