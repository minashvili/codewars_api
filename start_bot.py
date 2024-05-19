
import os
from dotenv import load_dotenv
import sqlite3
import random
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import threading


get_problem = ''
cout_done = 0

bot_api_key = os.getenv('SECRET_KEY')
bot = telebot.TeleBot(bot_api_key)


def get_id_with_out_solution(path_to_db: str) -> list[tuple]|None:

    try:
        sqlite_connection = sqlite3.connect(path_to_db)
        cursor = sqlite_connection.cursor()
        #print("connection to SQLite")
        sqlite_select_query = """SELECT id, ext_id FROM kata WHERE kata.solution IS ' ';"""
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


def insert_solution_to_db(path_to_db_update: str, username: str,  ext_id: str) -> None:
    
    parms = (username, ext_id)
    try:
        sqlite_connection = sqlite3.connect(path_to_db_update)
        cursor = sqlite_connection.cursor()
        sqlite_update_query = """UPDATE kata SET solution = solution || ' ' || ? WHERE ext_id = ?;"""
        cursor.execute(sqlite_update_query, parms)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error when working with SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
    
    return None

def super_reset() -> None:
    global cout_done
    cout_done = 0
    triz('')

@bot.message_handler(commands=['triz'])
def triz(message):

    global get_problem
    get_problem = randomly_select_id(get_id_with_out_solution('kata_from_codewars.db'))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Done")
    #btn2 = types.KeyboardButton("Statistics")
    markup.add(btn1)
    bot.send_message('-1002115846059', f"Радар Академии ТРИЗ 📡 зафексировал противоречие! \
                     {get_problem} ", reply_markup=markup) 
    

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Done':
        
        if message.from_user.last_name:
            get_name_user = f'{message.from_user.first_name} {message.from_user.last_name}'
        else:
            get_name_user = f'{message.from_user.first_name}'

        id_problem_codewars = get_problem.split('/')[-1]

        global cout_done

        if cout_done < 1:
            bot.send_message('-1002115846059', (
                f'Противоречию 👾{id_problem_codewars} нанесен первый удар!'
                f' Академия ТРИЗ гордится тобой {get_name_user}')) #Ответ бота
            #Выполнить запись в базу с решением добавлением ЮЗЕРА В ПОЛЕ РЕШЕНИЕ 
            insert_solution_to_db('kata_from_codewars.db', get_name_user, id_problem_codewars)
            cout_done += 1
            print(cout_done)

        elif cout_done <= 1:
            bot.send_message('-1002115846059', (
                f'Противоречию 👾{id_problem_codewars} нанесен решаюший удар!'
                f' Противоречие уничтожено! Так держать {get_name_user}!'))
            insert_solution_to_db('kata_from_codewars.db', get_name_user, id_problem_codewars)
            cout_done += 1            
            print(cout_done)
            # Тут задается следующее время, когда дернутся функции Триза triz('') и cout_done = 0
            timer = threading.Timer(random.randint(43200,172800), super_reset)
            timer.start()

        else:
            bot.send_message('-1002115846059', '📡 Подтверждение отсутствия противоречий.')
            #triz('')
            #cout_done = 0
            print(cout_done)

    elif message.text == 'New_problem': #(Тестовая херовина)
        triz('')
        cout_done = 0




load_dotenv()
triz('') 
bot.polling(none_stop=True, interval=0) 



#Функция threading должна 
#2 - задать рандомное вермя если ее вызвали и уйти в ансинхроное ожидание 



