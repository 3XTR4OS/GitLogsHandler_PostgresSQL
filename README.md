Программа, что обрабатывает гитхаб логи (пример 1) и добавляет их в PostgreSQL. Потом их можно использовать или выгрузить в каком-либо другом формате. Для этого нужно:
1) Залогиниться в psql: >>> psql -U username (по умолчанию postgres)
2) Подключиться к базе данных: >>> \connect database name
3) Использовать комманду copy: >>> \copy logs To 'D:/CSV.csv' With CSV DELIMITER ',' HEADER;

-----
Пример 1: 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

