from pathlib import Path
from tempfile import TemporaryDirectory


# Плохой пример: все тесты пишут в один общий файл.
SHARED_REPORT = Path("report.txt")


def write_shared_report(line: str) -> None:
    SHARED_REPORT.write_text(line, encoding="utf-8")


# Лучше: каждый тест получает свой isolated path.
def write_isolated_report(line: str) -> str:
    with TemporaryDirectory() as tmp_dir:
        report = Path(tmp_dir) / "report.txt"
        report.write_text(line, encoding="utf-8")
        return report.read_text(encoding="utf-8")


if __name__ == "__main__":
    print(write_isolated_report("stable"))
