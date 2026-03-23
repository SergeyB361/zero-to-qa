SQL_EXAMPLES = [
    "SELECT * FROM users;",
    "SELECT id, email FROM users WHERE active = 1;",
    "UPDATE users SET active = 0 WHERE id = 10;",
]

def show_sql_examples() -> None:
    for query in SQL_EXAMPLES:
        print(query)

if __name__ == "__main__":
    show_sql_examples()
