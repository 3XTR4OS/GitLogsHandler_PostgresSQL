import urllib.request
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
request = urllib.request.urlopen(URL)

try:
    # Подключение к БД
    connection = psycopg2.connect(
        user="postgres",
        password="0220",
        host="127.0.0.1",
        port="5432",
        database='data base')

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Cursor for performing database operations
    cursor = connection.cursor()

    # The use of indexes is due to the fact that the input data does not have a single separator.
    for row in request: 
        data = row.decode().strip().split() # Убирает лишние символы и пробелы.
        ip = data[0]
        time = data[3] + data[4]
        user_request = data[5] + data[6] + data[7]
        error_code = data[8] + ' ' + data[9]
        system_info = ''.join(data[11::])

        insert_query = \
            f"""INSERT INTO logs (IP, TIME, REQUEST, ERROR_CODE, SYSTEM_INFO) VALUES (
            '{ip}', '{time}', '{user_request}', '{error_code}', '{system_info}')"""

        cursor.execute(insert_query)
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка.", error)

finally:
    if connection:
        cursor.close()
        connection.close()
