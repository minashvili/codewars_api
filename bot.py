
import sqlite3
import random
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


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


bot = telebot.TeleBot('5157162549:AAEQe3F2rIuLgXwGw1yh3U_vfGyqt_uT5eM')
get_problem = randomly_select_id(get_id_with_out_solution('kata_from_codewars.db'))

@bot.message_handler(commands=['triz'])
def triz(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Done")
    markup.add(btn1)
    bot.send_message('-1002115846059', f"Радар Академии ТРИЗ 📡 зафексировал противоречие! \
                     {get_problem} ", reply_markup=markup) 
    

cout_done = 0

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    
    if message.text == 'Done':
        
        if message.from_user.last_name:
            get_name_user = f'{message.from_user.first_name} {message.from_user.last_name}'
        else:
            get_name_user = f'{message.from_user.first_name}'

        bot.send_message('-1002115846059', (
            f'Противоречие 👾{get_problem.split('/')[-1]} уничтожено!'
            f'Академия ТРИЗ гордится тобой {get_name_user}')) #ответ бота
        #Выполнить запись в базу с решением добавлением ЮЗЕРА В ПОЛЕ РЕШЕНИЕ или что-то такое 
        global cout_done
        cout_done += 1

        if cout_done > 2:
            bot.send_message('-1002115846059', 'Счетчик уничтожения противоречия больше двух, сигнал Академии ТРИЗ успешно терминируется')
            


triz('')
bot.polling(none_stop=True, interval=0) 




#Скрипт после двух Done должен или переставать работать или не отвечать на сообщения 
#Если скрипт всегда в сети то надо дергать функция triz('') для получения новой задачи 
#





