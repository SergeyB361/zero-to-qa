from __future__ import annotations

from pathlib import Path
from typing import Protocol


class UserRepo(Protocol):
    def save(self, user: dict[str, str]) -> dict[str, str]:
        ...


class Mailer(Protocol):
    def send_welcome(self, email: str) -> None:
        ...


def calculate_discount(total: float, is_vip: bool, coupon: str | None = None) -> float:
    if total < 0:
        raise ValueError("total must be non-negative")

    result = total
    if is_vip:
        result *= 0.9

    if coupon == "SALE10":
        result *= 0.9
    elif coupon == "SALE5":
        result *= 0.95
    elif coupon is not None:
        raise ValueError("unsupported coupon")

    return round(result, 2)


def register_user(email: str, role: str, repo: UserRepo, mailer: Mailer) -> dict[str, str]:
    if "@" not in email:
        raise ValueError("invalid email")

    if role not in {"user", "admin", "guest"}:
        raise ValueError("unsupported role")

    user = {"email": email, "role": role}
    saved_user = repo.save(user)
    mailer.send_welcome(email)
    return saved_user


def write_audit_report(lines: list[str], target_dir: Path) -> Path:
    target_dir.mkdir(parents=True, exist_ok=True)
    report_path = target_dir / "audit_report.txt"
    content = "\n".join(lines)
    report_path.write_text(content, encoding="utf-8")
    return report_path


def build_invite_code(email: str, rng) -> str:
    prefix = email.split("@")[0].upper()
    return f"{prefix}-{rng.randint(1000, 9999)}"
