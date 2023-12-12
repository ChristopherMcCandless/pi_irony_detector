# pi_irony_detector
Определяет наличие иронии в тексте

## [Подробная документация](docs/Doc.md)

### Решение включает в себя:
 - предобученную модель [twitter-roberta-base-irony](https://huggingface.co/cardiffnlp/twitter-roberta-base-irony)
 - web-клиент предоставлющий GUI для взаимодействия пользователя с модель, реализованный с помощью библиотеки streamlit
 - web-api реализованный с помощью библиотеки fastapi

### Структура проекта:
```
.
├── ...
├── docs            # Документация, примеры использования 
├── src
│   ├── services    # сервисы инкапсулирующие работу с моделями
│   ├── web         # web-client
│   └── api         # api
└── tests           # unit/integration tests
```
