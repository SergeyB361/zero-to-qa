import subprocess


def main() -> None:
    commands = [
        'psql -h localhost -U postgres -d zero_to_qa',
        r'\dt',
        r'\d tasks',
        "psql -h localhost -U postgres -d zero_to_qa -f postgres_lab/init/001_schema.sql",
    ]
    for line in commands:
        print(line)


if __name__ == '__main__':
    main()