# API: продвинутый уровень, День 5 — Contract testing

## Зачем это нужно
- Contract testing защищает интеграцию между consumer и provider от drift.
- Эта техника особенно ценна в распределённых системах и между командами.
- Она помогает ловить ломающее изменение до релиза.

## Что важно понять
- Contract — это обещание формата и поведения интерфейса.
- Важно проверять required fields, типы, enum и backward compatibility.
- Consumer expectations и provider response должны быть согласованы явно.

## Частые ошибки
- Считать contract testing полной заменой интеграционных тестов.
- Игнорировать backward compatibility.
- Проверять только один удачный payload.

## Практика дня
Открой practice.py и сравни ожидаемый контракт с фактическим payload.
