import flet as flet
import psycopg2 as ps
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
def platoky_data():
    connection = ps.connect(host=os.getenv("DBHOST"), database=os.getenv("DBNAMEOLD"),
                        user=os.getenv("DBUSERNAME"), password=os.getenv("DBPASSWORD"), port=os.getenv("DBPORT"))
    zapros = "SELECT * FROM ПППЛАТКИ ORDER BY Название ASC;"
    cursor = connection.cursor()
    # отправить запрос системе управления
    cursor.execute(zapros)
    records = cursor.fetchall()
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    return records
connection = ps.connect(host=os.getenv("DBHOST"), database=os.getenv("DBNAMEOLD"),
user=os.getenv("DBUSERNAME"), password=os.getenv("DBPASSWORD"), port=os.getenv("DBPORT"))
#ТАБЛИЦА ПО ПЛАТКАМ:
table_colums=[
            flet.DataColumn(flet.Text("Артикул")),
            flet.DataColumn(flet.Text("Название")),
            flet.DataColumn(flet.Text("Автор платка")),
            flet.DataColumn(flet.Text("Колорит 1")),
            flet.DataColumn(flet.Text("Колорит 2")),
            flet.DataColumn(flet.Text("Колорит 3")),
            flet.DataColumn(flet.Text("Колорит 4")),
            flet.DataColumn(flet.Text("Колорит 5")),
            flet.DataColumn(flet.Text("Узор темени")),
            flet.DataColumn(flet.Text("Узор сердцевины")),
            flet.DataColumn(flet.Text("Узор сторон")),
            flet.DataColumn(flet.Text("Узор углов")),
            flet.DataColumn(flet.Text("Узор краёв")),
            flet.DataColumn(flet.Text("Соотношение рисунка и орнамента")),
            flet.DataColumn(flet.Text("Нарисованный цветок 1")),
            flet.DataColumn(flet.Text("Нарисованный цветок 2")),
            flet.DataColumn(flet.Text("Нарисованный цветок 3")),
            flet.DataColumn(flet.Text("Нарисованный цветок 4")),
            flet.DataColumn(flet.Text("Нарисованный цветок 5")),
            flet.DataColumn(flet.Text("Размер платка")),
            flet.DataColumn(flet.Text("Материал платка")),
            flet.DataColumn(flet.Text("Материал бахромы"))]
#ЗДЕСЬ СТИЛИЗАЦИЯ ТАБЛИЦЫ ИМЕННО В ФЛЕТЕ
data_tablePR = flet.DataTable(heading_row_color=flet.Colors.BLUE_100,
                            border=flet.Border(bottom=flet.BorderSide(2, flet.Colors.BLUE),
                                               left=flet.BorderSide(2, flet.Colors.BLUE),
                                               right=flet.BorderSide(2, flet.Colors.BLUE)),
                            vertical_lines=flet.BorderSide(2, flet.Colors.BLUE),
                            horizontal_lines=flet.BorderSide(10, flet.Colors.BLUE), columns=table_colums, rows=[])
#      НАПОЛНЕНИЕ ТАБЛИЦЫ ДАННЫМИ
zapros = "SELECT * FROM ПППЛАТКИ ORDER BY Название ASC;"
cursor = connection.cursor()
# отправить запрос системе управления
cursor.execute(zapros)
records = cursor.fetchall()
if cursor:
    cursor.close()
if connection:
    connection.close()
for record in records:
    data_tablePR.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text(record[0])),
                                               flet.DataCell(flet.Text(record[1])),
                                               flet.DataCell(flet.Text(record[2])),
                                               flet.DataCell(flet.Text(record[3])),
                                               flet.DataCell(flet.Text(record[4])),
                                               flet.DataCell(flet.Text(record[5])),
                                               flet.DataCell(flet.Text(record[6])),
                                               flet.DataCell(flet.Text(record[7])),
                                               flet.DataCell(flet.Text(record[8])),
                                               flet.DataCell(flet.Text(record[9])),
                                               flet.DataCell(flet.Text(record[10])),
                                               flet.DataCell(flet.Text(record[11])),
                                               flet.DataCell(flet.Text(record[12])),
                                               flet.DataCell(flet.Text(record[13])),
                                               flet.DataCell(flet.Text(record[14])),
                                               flet.DataCell(flet.Text(record[15])),
                                               flet.DataCell(flet.Text(record[16])),
                                               flet.DataCell(flet.Text(record[17])),
                                               flet.DataCell(flet.Text(record[18])),
                                               flet.DataCell(flet.Text(record[19])),
                                               flet.DataCell(flet.Text(record[20])),
                                               flet.DataCell(flet.Text(record[21])), ], ))
async def platoky_tehnik():
    connection = ps.connect(host=os.getenv("DBHOST"), database=os.getenv("DBNAMEOLD"),
                        user=os.getenv("DBUSERNAME"), password=os.getenv("DBPASSWORD"), port=os.getenv("DBPORT"))
        #ТАБЛИЦА ПО ПЛАТКАМ:
    table_colums=[
            flet.DataColumn(flet.Text("Артикул")),
            flet.DataColumn(flet.Text("Название")),
            flet.DataColumn(flet.Text("Автор платка")),
            flet.DataColumn(flet.Text("Колорит 1")),
            flet.DataColumn(flet.Text("Колорит 2")),
            flet.DataColumn(flet.Text("Колорит 3")),
            flet.DataColumn(flet.Text("Колорит 4")),
            flet.DataColumn(flet.Text("Колорит 5")),
            flet.DataColumn(flet.Text("Узор темени")),
            flet.DataColumn(flet.Text("Узор сердцевины")),
            flet.DataColumn(flet.Text("Узор сторон")),
            flet.DataColumn(flet.Text("Узор углов")),
            flet.DataColumn(flet.Text("Узор краёв")),
            flet.DataColumn(flet.Text("Соотношение рисунка и орнамента")),
            flet.DataColumn(flet.Text("Нарисованный цветок 1")),
            flet.DataColumn(flet.Text("Нарисованный цветок 2")),
            flet.DataColumn(flet.Text("Нарисованный цветок 3")),
            flet.DataColumn(flet.Text("Нарисованный цветок 4")),
            flet.DataColumn(flet.Text("Нарисованный цветок 5")),
            flet.DataColumn(flet.Text("Размер платка")),
            flet.DataColumn(flet.Text("Материал платка")),
            flet.DataColumn(flet.Text("Материал бахромы"))]
    #ЗДЕСЬ СТИЛИЗАЦИЯ ТАБЛИЦЫ ИМЕННО В ФЛЕТЕ
    data_tableTH = flet.DataTable(heading_row_color=flet.Colors.BLUE_100,
                            border=flet.Border(bottom=flet.BorderSide(2, flet.Colors.BLUE),
                                               left=flet.BorderSide(2, flet.Colors.BLUE),
                                               right=flet.BorderSide(2, flet.Colors.BLUE)),
                            vertical_lines=flet.BorderSide(2, flet.Colors.BLUE),
                            horizontal_lines=flet.BorderSide(10, flet.Colors.BLUE), columns=table_colums, rows=[])
    #      НАПОЛНЕНИЕ ТАБЛИЦЫ ДАННЫМИ
    zapros = "SELECT * FROM ПППЛАТКИ ORDER BY Название ASC;"
    cursor = connection.cursor()
    # отправить запрос системе управления
    cursor.execute(zapros)
    records = cursor.fetchall()
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    for record in records:
        data_tablePR.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text(record[0])),
                                               flet.DataCell(flet.Text(record[1])),
                                               flet.DataCell(flet.Text(record[2])),
                                               flet.DataCell(flet.Text(record[3])),
                                               flet.DataCell(flet.Text(record[4])),
                                               flet.DataCell(flet.Text(record[5])),
                                               flet.DataCell(flet.Text(record[6])),
                                               flet.DataCell(flet.Text(record[7])),
                                               flet.DataCell(flet.Text(record[8])),
                                               flet.DataCell(flet.Text(record[9])),
                                               flet.DataCell(flet.Text(record[10])),
                                               flet.DataCell(flet.Text(record[11])),
                                               flet.DataCell(flet.Text(record[12])),
                                               flet.DataCell(flet.Text(record[13])),
                                               flet.DataCell(flet.Text(record[14])),
                                               flet.DataCell(flet.Text(record[15])),
                                               flet.DataCell(flet.Text(record[16])),
                                               flet.DataCell(flet.Text(record[17])),
                                               flet.DataCell(flet.Text(record[18])),
                                               flet.DataCell(flet.Text(record[19])),
                                               flet.DataCell(flet.Text(record[20])),
                                               flet.DataCell(flet.Text(record[21])), ], ))
    return data_tableTH
async def platoky_marketolog():
    connection = ps.connect(host=os.getenv("DBHOST"), database=os.getenv("DBNAMEOLD"),
                        user=os.getenv("DBUSERNAME"), password=os.getenv("DBPASSWORD"), port=os.getenv("DBPORT"))
        #ТАБЛИЦА ПО ПЛАТКАМ:
    table_colums=[
            flet.DataColumn(flet.Text("Артикул")),
            flet.DataColumn(flet.Text("Название")),
            flet.DataColumn(flet.Text("Автор платка")),
            flet.DataColumn(flet.Text("Колорит 1")),
            flet.DataColumn(flet.Text("Колорит 2")),
            flet.DataColumn(flet.Text("Колорит 3")),
            flet.DataColumn(flet.Text("Колорит 4")),
            flet.DataColumn(flet.Text("Колорит 5")),
            flet.DataColumn(flet.Text("Узор темени")),
            flet.DataColumn(flet.Text("Узор сердцевины")),
            flet.DataColumn(flet.Text("Узор сторон")),
            flet.DataColumn(flet.Text("Узор углов")),
            flet.DataColumn(flet.Text("Узор краёв")),
            flet.DataColumn(flet.Text("Соотношение рисунка и орнамента")),
            flet.DataColumn(flet.Text("Нарисованный цветок 1")),
            flet.DataColumn(flet.Text("Нарисованный цветок 2")),
            flet.DataColumn(flet.Text("Нарисованный цветок 3")),
            flet.DataColumn(flet.Text("Нарисованный цветок 4")),
            flet.DataColumn(flet.Text("Нарисованный цветок 5")),
            flet.DataColumn(flet.Text("Размер платка")),
            flet.DataColumn(flet.Text("Материал платка")),
            flet.DataColumn(flet.Text("Материал бахромы"))]
    #ЗДЕСЬ СТИЛИЗАЦИЯ ТАБЛИЦЫ ИМЕННО В ФЛЕТЕ
    data_tableMK = flet.DataTable(heading_row_color=flet.Colors.BLUE_100,
                            border=flet.Border(bottom=flet.BorderSide(2, flet.Colors.BLUE),
                                               left=flet.BorderSide(2, flet.Colors.BLUE),
                                               right=flet.BorderSide(2, flet.Colors.BLUE)),
                            vertical_lines=flet.BorderSide(2, flet.Colors.BLUE),
                            horizontal_lines=flet.BorderSide(10, flet.Colors.BLUE), columns=table_colums, rows=[])
    #      НАПОЛНЕНИЕ ТАБЛИЦЫ ДАННЫМИ
    zapros = "SELECT * FROM ПППЛАТКИ ORDER BY Название ASC;"
    cursor = connection.cursor()
    # отправить запрос системе управления
    cursor.execute(zapros)
    records = cursor.fetchall()
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    for record in records:
        data_tableMK.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text(record[0])),
                                               flet.DataCell(flet.Text(record[1])),
                                               flet.DataCell(flet.Text(record[2])),
                                               flet.DataCell(flet.Text(record[3])),
                                               flet.DataCell(flet.Text(record[4])),
                                               flet.DataCell(flet.Text(record[5])),
                                               flet.DataCell(flet.Text(record[6])),
                                               flet.DataCell(flet.Text(record[7])),
                                               flet.DataCell(flet.Text(record[8])),
                                               flet.DataCell(flet.Text(record[9])),
                                               flet.DataCell(flet.Text(record[10])),
                                               flet.DataCell(flet.Text(record[11])),
                                               flet.DataCell(flet.Text(record[12])),
                                               flet.DataCell(flet.Text(record[13])),
                                               flet.DataCell(flet.Text(record[14])),
                                               flet.DataCell(flet.Text(record[15])),
                                               flet.DataCell(flet.Text(record[16])),
                                               flet.DataCell(flet.Text(record[17])),
                                               flet.DataCell(flet.Text(record[18])),
                                               flet.DataCell(flet.Text(record[19])),
                                               flet.DataCell(flet.Text(record[20])),
                                               flet.DataCell(flet.Text(record[21])), ], ))
    return data_tableMK
#ТАБЛИЦА ПО ПОСЕЩЕНИЯМ:
table2_colums = [flet.DataColumn(flet.Text("Артикул")),
                 flet.DataColumn(flet.Text("Дата и время посещения")),
                 flet.DataColumn(flet.Text("IP-пользователя")),
                 flet.DataColumn(flet.Text("Запрашиваемый ресурс")),
                 flet.DataColumn(flet.Text("Статус")),
                 flet.DataColumn(flet.Text("Время исполнения"))]
#ОФОРМЛЕНИЕ ТАБЛИЦЫ ИМЕННО В ФЛЕТ
data_table2 = flet.DataTable(heading_row_color=flet.Colors.BLUE_100,
                                    border=flet.Border(bottom=flet.BorderSide(2, flet.Colors.BLUE),
                                                       left=flet.BorderSide(2, flet.Colors.BLUE),
                                                       right=flet.BorderSide(2, flet.Colors.BLUE)),
                                    vertical_lines=flet.BorderSide(2, flet.Colors.BLUE),
                                    horizontal_lines=flet.BorderSide(10, flet.Colors.BLUE), columns=table2_colums,
                                    rows=[])
connection = ps.connect(host=os.getenv("DBHOST"), database=os.getenv("DBNAMEOLD"),
                        user=os.getenv("DBUSERNAME"), password=os.getenv("DBPASSWORD"), port=os.getenv("DBPORT"))
cursor = connection.cursor()
zapros2 = "SELECT * FROM Журнал_Посещений ORDER BY Время_Посещения ASC;"
# отправить запрос системе управления
cursor.execute(zapros2)
records = cursor.fetchall()
if cursor:
    cursor.close()
if connection:
    connection.close()
    for record in records:
        data_table2.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text(record[0])),
                                                        flet.DataCell(flet.Text(record[1])),
                                                        flet.DataCell(flet.Text(record[2])),
                                                        flet.DataCell(flet.Text(record[3])),
                                                        flet.DataCell(flet.Text(record[4])),
                                                        flet.DataCell(flet.Text(record[5])), ], ))
table3_colums = [flet.DataColumn(flet.Text("Артикул")),
                         flet.DataColumn(flet.Text("Индефикатор_Автора")),
                         flet.DataColumn(flet.Text("Автор_Отзыва")),
                         flet.DataColumn(flet.Text("Текст_Отзыва")),
                         flet.DataColumn(flet.Text("Время_Записи_Отзыва")),
                         flet.DataColumn(flet.Text("Секунды_Записи_Отзыва"))]
data_table3=flet.DataTable(heading_row_color=flet.Colors.BLUE_100,
                                    border=flet.Border(bottom=flet.BorderSide(2, flet.Colors.BLUE),
                                                       left=flet.BorderSide(2, flet.Colors.BLUE),
                                                       right=flet.BorderSide(2, flet.Colors.BLUE)),
                                    vertical_lines=flet.BorderSide(2, flet.Colors.BLUE),
                                    horizontal_lines=flet.BorderSide(10, flet.Colors.BLUE), columns=table3_colums,
                                    rows=[])
connection = ps.connect(host=os.getenv("DBHOST"), database=os.getenv("DBNAMEOLD"),
                        user=os.getenv("DBUSERNAME"), password=os.getenv("DBPASSWORD"), port=os.getenv("DBPORT"))
cursor = connection.cursor()
zapros3 = "SELECT * FROM Книга_Отзывов ORDER BY Время_Записи_Отзыва ASC;"
# отправить запрос системе управления
cursor.execute(zapros3)
records = cursor.fetchall()
if cursor:
    cursor.close()
if connection:
    connection.close()
for record in records:
    data_table3.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text(record[0])),
                                                        flet.DataCell(flet.Text(record[1])),
                                                        flet.DataCell(flet.Text(record[2])),
                                                        flet.DataCell(flet.Text(record[3])),
                                                        flet.DataCell(flet.Text(record[4])),
                                                        flet.DataCell(flet.Text(record[5])), ], ))