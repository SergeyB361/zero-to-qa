# ТЗ: Мини-проект — Advanced API suite

## Исходный файл
Используй:
- orders_api.py

## Цель проекта
Построить компактный API suite, который покрывает auth, negative paths, contract checks и stateful сценарии.

## Deliverables
- tests или demo_scenarios.py с позитивными и негативными кейсами
- helper для auth headers или token handling
- contract checks для order payload
- минимум один stateful сценарий

## Обязательные требования
- покрыть 401 и 404 сценарии
- добавить минимум одну validation negative проверку
- валидировать order payload по required fields и status values
- stateful сценарий должен иметь allowed и forbidden path

## Формат сдачи
- файлы решения и инструкция запуска
- показать вывод минимум трёх сценариев
- объяснить, где auth, contract и negative слой

## Рубрика оценки (10 баллов)
- 2 балла — покрыты auth и basic error paths
- 2 балла — contract checks не сводятся к одному assert
- 2 балла — negative scenarios проверяют не только status code
- 2 балла — stateful сценарий читается как lifecycle сущности
- 2 балла — suite компактен и понятен

## Что особенно проверяется
- решение должно быть структурным, а не набором случайных заметок
- каждое принятое решение должно быть объяснимо через риск, цель или качество
- материал должен быть пригоден для ревью и дальнейшего расширения
