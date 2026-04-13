# Практика: test oracles

PROMPTS = {'scenario_to_oracle': 'Опиши минимум три сценария как список словарей {scenario, oracle_source, '
                       'expected_result}.',
 'weak_oracle_risks': 'Перечисли минимум два риска слабого oracle.'}

SUBMISSION = {'scenario_to_oracle': [], 'weak_oracle_risks': []}

RULES = {'scenario_to_oracle': {'type': 'list_of_dicts',
                        'min_items': 3,
                        'required_keys': ['scenario', 'oracle_source', 'expected_result'],
                        'keywords': ['oracle']},
 'weak_oracle_risks': {'type': 'list', 'min_items': 2, 'keywords': ['expected', 'guess']}}


def flatten(value: object) -> str:
    if isinstance(value, dict):
        parts: list[str] = []
        for key, item in value.items():
            parts.append(str(key))
            parts.append(flatten(item))
        return ' '.join(parts).lower()
    if isinstance(value, list):
        return ' '.join(flatten(item) for item in value).lower()
    return str(value).lower()


def has_value(value: object) -> bool:
    if isinstance(value, dict):
        return all(has_value(item) for item in value.values()) if value else False
    if isinstance(value, list):
        return len(value) > 0 and all(has_value(item) for item in value)
    return bool(str(value).strip())


def validate_field(name: str, value: object, rule: dict[str, object]) -> list[tuple[str, bool]]:
    results: list[tuple[str, bool]] = []
    rule_type = str(rule.get('type', 'text'))
    text = flatten(value)
    keywords = [str(item).lower() for item in rule.get('keywords', [])]

    if rule_type == 'list':
        min_items = int(rule.get('min_items', 1))
        results.append((f'{name} min_items', isinstance(value, list) and len(value) >= min_items))
    elif rule_type == 'dict':
        required_keys = [str(item) for item in rule.get('required_keys', [])]
        ok = isinstance(value, dict) and all(key in value and has_value(value[key]) for key in required_keys)
        results.append((f'{name} required_keys', ok))
    elif rule_type == 'list_of_dicts':
        required_keys = [str(item) for item in rule.get('required_keys', [])]
        min_items = int(rule.get('min_items', 1))
        ok = isinstance(value, list) and len(value) >= min_items
        if ok:
            ok = all(isinstance(item, dict) and all(key in item and has_value(item[key]) for key in required_keys) for item in value)
        results.append((f'{name} structured_rows', ok))
    else:
        min_words = int(rule.get('min_words', 6))
        results.append((f'{name} min_words', len(text.split()) >= min_words))
        if keywords:
            detail_words = int(rule.get('detail_words', max(12, len(keywords) * 4)))
            keyword_ok = all(keyword in text for keyword in keywords)
            detail_ok = len(text.split()) >= detail_words
            results.append((f'{name} keywords_or_detail', keyword_ok or detail_ok))
    return results


def run_checks() -> list[tuple[str, bool]]:
    results: list[tuple[str, bool]] = []
    for field_name, rule in RULES.items():
        results.extend(validate_field(field_name, SUBMISSION[field_name], rule))
    return results


if __name__ == '__main__':
    print('Заполни SUBMISSION и затем снова запусти файл.')
    for field_name, prompt in PROMPTS.items():
        print(f'[{field_name}] {prompt}')
        print('Current value:', SUBMISSION[field_name])
        print('---')
    print('Checks:')
    for name, status in run_checks():
        print(f'{name}: {status}')
