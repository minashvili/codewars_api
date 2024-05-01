
from site_parser import challenges
import sqlite3


def work_with_db(data_from_codewars: list[dict]) -> str|None:

    #For cycle writing to the database?
    #Here you need to apply SQL query parameters

    for one_kata in data_from_codewars:
        parms = (one_kata['id'], one_kata['name'])

        try:
            sqlite_connection = sqlite3.connect('kata_from_codewars.db')
            cursor = sqlite_connection.cursor()
            print("connection to SQLite")

            sqlite_insert_query = """INSERT INTO kata
                                (ext_id, name)
                                VALUES
                                (?, ?);"""
            
            count = cursor.execute(sqlite_insert_query, parms)
            sqlite_connection.commit()

            print("The record was successfully inserted into the kata table", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Error when working with SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Connection to SQLite closed")
