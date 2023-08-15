#### Запуск проекта в dev-режиме

- Склонируйте репозиторий:  
``` git clone <название репозитория> ```    
- Установите и активируйте виртуальное окружение:  
``` python -m venv venv ```  
``` source venv/Scripts/activate ``` 
- Установите зависимости из файла requirements.txt:   
``` pip install -r requirements.txt ```
- Перейдите в папку api/test/
``` cd api_test/ ```
- Выполните команду:   
``` python manage.py runserver ```

#### Отправка запроса

``` GET /api/v1/ping/ ```  
