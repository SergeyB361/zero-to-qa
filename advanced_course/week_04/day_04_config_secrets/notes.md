# API: reliability и integration, День 4 — Config и secrets

## Зачем это нужно
Надёжный test framework не должен хранить base URL, token и credentials прямо в коде. Конфигурация должна меняться между окружениями без редактирования файлов.

## Что важно понять
Обычно удобно разделять:
- config: base URL, timeout, feature flags
- secrets: API tokens, passwords, private keys

Хорошая практика:
- читать config из env vars или config files
- хранить sensible defaults только для безопасных значений
- не логировать секреты полностью

## Частые ошибки
- захардкодить токен в examples и tests
- считать отсутствие секрета допустимым для любого сценария
- смешивать prod и local конфиг в одном наборе значений

## Что запомнить
- секреты не должны жить в git
- base URL и token должны приходить извне
- framework должен иметь понятный missing-config behavior
- логировать нужно факт наличия, а не полный секрет

## Практика дня
Открой practice.py и собери простую модель config loader с env vars.
