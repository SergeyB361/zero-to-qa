def payment_provider_mock(status: str) -> tuple[int, dict[str, object]]:
    if status == 'timeout':
        return 504, {'error': 'timeout'}
    if status == 'declined':
        return 402, {'error': 'payment declined'}
    return 200, {'transaction_id': 'tx-1', 'status': 'approved'}


if __name__ == '__main__':
    print(payment_provider_mock('declined'))
    print(payment_provider_mock('approved'))
