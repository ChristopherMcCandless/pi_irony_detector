## WEB-клиент
### Для запуска:
```> streamlit run src/web/main.py```
### Пример работы:
![](example_web_1.png)

## Web-API
### Endpoints:
 - "/detect-irony/" , 
    контракт:
     - request - { text_to_detect: "text bla bla" } 
     - response - { "non-irony": score, "irony": score }
 ### Примеры:
 ![Alt text](example_api_1.png)
 ![Alt text](example_api_2.png)

