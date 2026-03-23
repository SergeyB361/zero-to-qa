def docker_run_command(image: str, port: int) -> str:
    return f"docker run -p {port}:{port} {image}"


if __name__ == "__main__":
    print(docker_run_command("postgres:16", 5432))
