# FastAPI + SQLAlchemy Integration

## Когда это нужно
Это точка, где отдельные курсы соединяются: FastAPI даёт request lifecycle, SQLAlchemy даёт data layer, а dependency system связывает их без глобальных session singleton-ов.

## Как об этом думать
Обычная схема такая:
1. есть `SessionLocal`;
2. есть dependency `get_session()`;
3. route получает `session: Session = Depends(get_session)`;
4. service/repository работают с этой session;
5. после request session закрывается.

## Что важно понять
- route не должен сам создавать engine;
- session dependency — это boundary between web layer and data layer;
- commit policy должна быть явной.
