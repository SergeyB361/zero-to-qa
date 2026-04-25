"""
Практическое задание:
1. Реализуй salted password hashing helper.
2. Создай user payload без хранения raw password.
3. Реализуй verify helper для correct/wrong password.

Например:
- `build_user_record('qa@example.com', 'TestPass123')` -> dict c `email`, `password_hash`, `password_salt`, `role`
- raw password в payload быть не должно
- `verify_password(...)` -> `True` для correct password и `False` для wrong password

Критерий готовности: `run_checks()` проходит без ошибок.
"""

import hashlib
from dataclasses import dataclass


@dataclass(slots=True)
class UserRecord:
    email: str
    password_hash: str
    password_salt: str
    role: str = 'user'



def hash_password(password: str, salt: str) -> str:
    # TODO: вернуть pbkdf2_hmac hex digest для password + salt.
    return 'TODO'



def build_user_record(email: str, password: str, role: str = 'user') -> UserRecord:
    salt = 'fixed-practice-salt'
    # TODO: собрать UserRecord без хранения raw password.
    return UserRecord(email=email, password_hash='TODO', password_salt='TODO', role=role)



def verify_password(user: UserRecord, candidate_password: str) -> bool:
    # TODO: пересчитать hash и сравнить с сохранённым.
    return False



def run_checks() -> None:
    user = build_user_record('qa@example.com', 'TestPass123', role='manager')
    expected_hash = hashlib.pbkdf2_hmac(
        'sha256',
        b'TestPass123',
        b'fixed-practice-salt',
        100_000,
    ).hex()

    assert user.email == 'qa@example.com', 'email should be stored in user record'
    assert user.role == 'manager', 'role should be stored in user record'
    assert user.password_salt == 'fixed-practice-salt', 'salt should be stored in user record'
    assert user.password_hash == expected_hash, 'password hash is incorrect'
    assert not hasattr(user, 'password'), 'raw password should not be stored in user record'
    assert verify_password(user, 'TestPass123') is True, 'correct password should pass verification'
    assert verify_password(user, 'WrongPass123') is False, 'wrong password should fail verification'


if __name__ == '__main__':
    try:
        run_checks()
    except AssertionError as exc:
        print(f'Self-check failed: {exc}')
        raise
    print('Practice checks passed')
