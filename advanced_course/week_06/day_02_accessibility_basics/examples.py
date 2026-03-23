def is_accessible_button(node: dict[str, str]) -> bool:
    return node.get("role") == "button" and bool(node.get("name"))


if __name__ == "__main__":
    print(is_accessible_button({"role": "button", "name": "Save"}))
