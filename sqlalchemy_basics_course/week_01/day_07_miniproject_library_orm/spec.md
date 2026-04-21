# Library ORM — Spec

Нужно реализовать:
1. модель `Author`
2. модель `Book`
3. one-to-many связь `Author -> Book`
4. функцию `seed_library(session)`
5. функцию `list_books_with_authors(session)`
6. функцию `create_book(session, author_name, title)`

Ожидаемый smoke-flow:
- initial list содержит seeded books
- `create_book(...)` добавляет новую книгу
- повторный list отражает изменение
