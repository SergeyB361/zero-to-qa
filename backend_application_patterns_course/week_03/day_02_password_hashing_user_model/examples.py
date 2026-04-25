import hashlib
import secrets
from dataclasses import dataclass


@dataclass(slots=True)
class UserRecord:
    email: str
    password_hash: str
    password_salt: str
    role: str = 'user'



def hash_password(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100_000).hex()



def make_user(email: str, password: str, role: str = 'user') -> UserRecord:
    salt = secrets.token_hex(8)
    return UserRecord(
        email=email,
        password_hash=hash_password(password, salt),
        password_salt=salt,
        role=role,
    )



def verify_password(user: UserRecord, candidate_password: str) -> bool:
    return hash_password(candidate_password, user.password_salt) == user.password_hash


if __name__ == '__main__':
    user = make_user('anna@example.com', 'StrongPass123', role='admin')
    print('USER ->', {'email': user.email, 'role': user.role, 'hash_length': len(user.password_hash)})
    print('VERIFY CORRECT ->', verify_password(user, 'StrongPass123'))
    print('VERIFY WRONG ->', verify_password(user, 'wrong-password'))
