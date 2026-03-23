# ТЗ: Мини-проект — Requirements to test design pack

## Исходный файл
Используй:
- requirements.md

## Цель проекта
Преобразовать исходные требования в пакет тест-дизайна: EARS, decision tables, state model, pairwise и user flows.

## Deliverables
- переписанные требования в формате EARS
- decision table минимум для одного правила
- state machine или state transition table
- pairwise или компактный combinatorial набор
- use cases или user flows

## Обязательные требования
- есть явная связь между requirement и артефактами
- decision table покрывает meaningful combinations правила
- state model различает allowed и forbidden transitions
- pairwise объяснён, а не дан случайным набором

## Формат сдачи
- markdown-файлы или один consolidated document
- явные связи между requirement и артефактами
- показать одно правило, разобранное тремя техниками

## Рубрика оценки (10 баллов)
- 2 балла — требования переписаны без двусмысленности
- 2 балла — decision table полезна, а не декоративна
- 2 балла — state model отражает реальный workflow
- 2 балла — pairwise/use flows уменьшают лишние комбинации осознанно
- 2 балла — пакет можно использовать как основу для test cases

## Что особенно проверяется
- решение должно быть структурным, а не набором случайных заметок
- каждое принятое решение должно быть объяснимо через риск, цель или качество
- материал должен быть пригоден для ревью и дальнейшего расширения
