# [{id:123, name: 'super-admin', level: 'hyomoyo-8'}, ...]


import sqlite3

try:
    sqlite_connection = sqlite3.connect('kata_from_codewars.db')
    cursor = sqlite_connection.cursor()
    print("connection to SQLite")

    sqlite_insert_query = """INSERT INTO kata
                          (id, name, level)
                          VALUES
                          (1, 'Test', 'hyomoyo-8');"""
    
    count = cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()

    print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")







