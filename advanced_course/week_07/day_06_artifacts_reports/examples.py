def artifact_bundle(test_name: str) -> dict[str, str]:
    return {
        "log": f"artifacts/{test_name}.log",
        "xml": f"artifacts/{test_name}.xml",
        "trace": f"artifacts/{test_name}.zip",
    }


if __name__ == "__main__":
    print(artifact_bundle("test_api_order_create"))
