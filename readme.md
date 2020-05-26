<h3>Развёртывание проекта</h3>
- Клонируем репозиторий: <br>
    git clone https://github.com/GorskiiNikita/axis.git <br>
    cd axis <br>

- Создаём и активируем виртуальное окружение: <br>
    python3.7 -m venv venv <br>
    source venv/bin/activate <br>

- Устанавливаем зависимости: <br>
    pip install -r requirements.txt <br>

- Создаём миграции и выполняем их. После этого шага джанго сам создаст бд sqlite3 и определит там нужные таблицы: <br>
    python manage.py makemigrations <br>
    python manage.py migrate <br>

- Загрузим данные из интернета и сохраним в бд: <br>
    python manage.py load_data <br>


<h3>Работа с api</h3>
- Получить все записи: <br>
     /api/posts/ <br>
     
- Можно указать в строке запроса формат данных:  <br>
    /api/posts/?format=json - получить json <br>
    /api/posts/?format=xlsx - получить xlsx <br>
    
- Фильтрация по дате. В строке запроса передаются параметры start_date и end_date. Можно передать один из параметров, тогда фильтрация будет от/до заданного параметра и до начала/конца. <br>
    /api/posts/?start_date=2008-05-13&end_date=2008-05-16&format=json - Получить все записи с 13 мая 2008 года по 16 мая 2008 года <br>
    /api/posts/?end_date=2008-05-16&format=json - Получить все записи от начала и до 16 мая 2008 года <br>
    /api/posts/?start_date=2008-05-16&format=json - Получить все записи от 16 мая 2008 года и до конца <br>



