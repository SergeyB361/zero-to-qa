def build_failure_bundle(test_name: str) -> dict[str, str]:
    return {
        "screenshot": f"artifacts/{test_name}.png",
        "trace": f"artifacts/{test_name}.zip",
        "html": f"artifacts/{test_name}.html",
    }


if __name__ == "__main__":
    print(build_failure_bundle("test_login"))
