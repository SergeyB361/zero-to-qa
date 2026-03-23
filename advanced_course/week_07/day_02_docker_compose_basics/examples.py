SERVICES = {
    "app": {"image": "my-app:latest", "ports": ["8080:8080"]},
    "db": {"image": "postgres:16", "ports": ["5432:5432"]},
}


if __name__ == "__main__":
    print(SERVICES)
