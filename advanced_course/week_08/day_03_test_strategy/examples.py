def choose_layers(has_ui: bool, has_api: bool) -> list[str]:
    layers = ["unit"]
    if has_api:
        layers.append("api")
    if has_ui:
        layers.append("ui-smoke")
    return layers


if __name__ == "__main__":
    print(choose_layers(True, True))
