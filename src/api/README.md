### Web сервис предоставляющий API "Обнаружение иронии в текстах"

## Endpoints:
 - "/detect-irony/" , 
    контракт:
     - request - { text_to_detect: "text bla bla" } 
     - response - { "non-irony": score, "irony": score }

## Структура проекта:
 - main.py - код приложения API - инфраструктура, контроллеры
 - irony_detector.py - модуль содержит класс инкапуслирующий логику взаимодействия с моделью

 ## Примеры вызова:
 ![Alt text](image.png)
 ![Alt text](image-3.png)

