from dataclasses import dataclass


@dataclass(frozen=True)
class SnapshotConfig:
    page_name: str
    browser: str
    viewport: tuple[int, int]
    ignore_line_prefixes: tuple[str, ...] = ()

    def baseline_key(self) -> str:
        width, height = self.viewport
        return f"{self.page_name}-{self.browser}-{width}x{height}.snap"


def normalize_render(render: str, ignore_line_prefixes: tuple[str, ...]) -> str:
    lines = []
    for raw_line in render.splitlines():
        line = raw_line.strip()
        if any(line.startswith(prefix) for prefix in ignore_line_prefixes):
            lines.append("<ignored-line>")
        else:
            lines.append(line)
    return "\n".join(lines)


def diff_ratio(left: str, right: str) -> float:
    max_len = max(len(left), len(right), 1)
    padded_left = left.ljust(max_len)
    padded_right = right.ljust(max_len)
    diff_count = sum(1 for a, b in zip(padded_left, padded_right) if a != b)
    return diff_count / max_len


def compare_snapshot(baseline: str, current: str, ignore_line_prefixes: tuple[str, ...], max_ratio: float) -> tuple[bool, float]:
    clean_baseline = normalize_render(baseline, ignore_line_prefixes)
    clean_current = normalize_render(current, ignore_line_prefixes)
    ratio = diff_ratio(clean_baseline, clean_current)
    return ratio <= max_ratio, ratio


if __name__ == "__main__":
    config = SnapshotConfig(
        page_name="checkout-summary",
        browser="chromium",
        viewport=(1280, 720),
        ignore_line_prefixes=("Generated at:",),
    )

    baseline = """
    Checkout Summary
    Total: 149.00
    Generated at: 2026-04-13 20:00
    Button: Pay now
    """.strip()

    same_layout_new_timestamp = """
    Checkout Summary
    Total: 149.00
    Generated at: 2026-04-13 20:07
    Button: Pay now
    """.strip()

    broken_layout = """
    Checkout Summary
    Total: 149.00
    Generated at: 2026-04-13 20:07
    Button: Pay later
    Sidebar overlaps content
    """.strip()

    raw_ok, raw_ratio = compare_snapshot(baseline, same_layout_new_timestamp, (), 0.0)
    stable_ok, stable_ratio = compare_snapshot(baseline, same_layout_new_timestamp, config.ignore_line_prefixes, 0.0)
    broken_ok, broken_ratio = compare_snapshot(baseline, broken_layout, config.ignore_line_prefixes, 0.10)

    print("baseline key:", config.baseline_key())
    print("raw compare passes:", raw_ok, "diff ratio:", round(raw_ratio, 3))
    print("normalized compare passes:", stable_ok, "diff ratio:", round(stable_ratio, 3))
    print("broken layout passes:", broken_ok, "diff ratio:", round(broken_ratio, 3))
    print()
    print("Meaning:")
    print("- dynamic lines should be normalized before compare")
    print("- same stable layout should keep the baseline green")
    print("- real visual shifts must still fail")