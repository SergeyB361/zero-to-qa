def diagnostic_record(method: str, url: str, status_code: int, trace_id: str) -> dict[str, object]:
    return {
        'method': method,
        'url': url,
        'status_code': status_code,
        'trace_id': trace_id,
    }


if __name__ == '__main__':
    print(diagnostic_record('GET', '/orders/1', 500, 'trace-123'))
