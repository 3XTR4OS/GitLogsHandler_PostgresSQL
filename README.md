Программа, что обрабатывает гитхаб логи (пример 1) и добавляет их в базу данных PostgreSQL. Потом с ними можно взаимодействовать путём SQL запросов. Например, чтобы выгрузить данные в CSV формат нужно:
1) Залогиниться в psql: >>> psql -U username (по умолчанию postgres)
2) Подключиться к базе данных: >>> \connect database_name
3) Использовать комманду copy: >>> \copy logs To 'D:/CSV.csv' With CSV DELIMITER ',' HEADER;

-----
Пример 1: 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

