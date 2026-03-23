from pathlib import Path
from tempfile import TemporaryDirectory


# Пример опасного shared state
GLOBAL_COUNTER = {"value": 0}


def increment_global_counter() -> int:
    GLOBAL_COUNTER["value"] += 1
    return GLOBAL_COUNTER["value"]


# Пример безопасного isolated ресурса
def create_report_copy(content: str) -> str:
    with TemporaryDirectory() as tmp_dir:
        path = Path(tmp_dir) / "report.txt"
        path.write_text(content, encoding="utf-8")
        return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    print(create_report_copy("xdist-safe"))
