import sqlite3
import random

def get_id_with_out_solution(path_to_db: str) -> list[tuple]|None:

    try:
        sqlite_connection = sqlite3.connect(path_to_db)
        cursor = sqlite_connection.cursor()
        #print("connection to SQLite")
        sqlite_select_query = """SELECT id, ext_id FROM kata WHERE kata.solution IS NULL;"""
        cursor.execute(sqlite_select_query)
        rows_from_kata = cursor.fetchall()
        #for row_from_kata in rows_from_kata:
        #print(type(rows_from_kata))
        cursor.close()

    except sqlite3.Error as error:
        print("Error when working with SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            #print("Connection to SQLite closed")
    
    return rows_from_kata
    #print(rows_from_kata)


def randomly_select_id(list_id_from_kata: list[tuple]) -> str:
    random_id = random.choice(list_id_from_kata)
    return f'https://www.codewars.com/kata/{random_id[1]}'


print(randomly_select_id(get_id_with_out_solution('kata_from_codewars.db')))

