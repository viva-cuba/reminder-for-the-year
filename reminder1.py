# Python 3.9.6 64-bit www.vivacuba1990.ru

import os
from gtts import gTTS
import random
import time
from turtle import *
import playsound
import speech_recognition as sr
from time import strftime
import locale
import keyboard as ked

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        print("слушаю тебя:")
        audio = r.listen(source)
        print('услышала: ')

    try:
        our_speech = r.recognize_google(audio, language="ru-RU").lower()
        print("вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError as e:
        say_message("проверь интернет")
        return "ошибка"
        
def do_tris_command(message):
    message = message.lower()    

    if "запиши напоминалку" in message:
            say_message('на какой день?')
            record = listen_command()
            record = record.replace('августа', '08').replace('сентября', '09').replace('октября', '10').replace('ноября', '11').replace('декабря', '12').replace('января', '01').replace('февраля', '02').replace('марта', '03').replace('апреля', '04').replace('мая', '05').replace('июня', '06').replace('июля', '07')
            current_date = record
            if len(record) == 4:
                current_date  = '0' + current_date
            if os.path.exists('REMINDER_BY_DAY/'+ current_date +'.txt'):   
                say_message('такой файл существует')
                file = open('REMINDER_BY_DAY/'+ current_date +'.txt', 'r', encoding='utf-8')
                f_all = file.read()
                say_message('читаю содержимое файла ' + f_all + ' файл прочитан, теперь можешь задать другую дату или добавить запись в этот файл')
                file.close() 
                return message
            say_message('говори, записываю')
            record_1 = listen_command()
            file = open('REMINDER_BY_DAY/'+ current_date +'.txt', 'w', encoding='utf-8')
            file.write(record_1)
            file.close()
            say_message('день напоминания ' + current_date + ' я записала в напоминалку '+ record_1)
            say_message('что то ещё?')
            # exit()

    elif "добавь запись" in message:
        say_message('на какой день?')
        record = listen_command()
        record = record.replace('августа', '08').replace('сентября', '09').replace('октября', '10').replace('ноября', '11').replace('декабря', '12').replace('января', '01').replace('февраля', '02').replace('марта', '03').replace('апреля', '04').replace('мая', '05').replace('июня', '06').replace('июля', '07')
        current_date = record
        if len(record) == 4:
            current_date  = '0' + current_date
        say_message('говори, записываю')
        record_1 = listen_command()
        file = open('REMINDER_BY_DAY/'+ current_date +'.txt', 'a', encoding='utf-8')
        file.write('\n' + record_1)
        file.close()
        say_message('я записала в напоминалку '+ record_1)
        say_message('что то ещё?')
        # exit()

    elif "удали файл" in message:
        os.startfile('C:/assistent_1/REMINDER_BY_DAY')
        say_message(str('какой файл удалить'))
        record = listen_command()
        record = record.replace('августа', '08').replace('сентября', '09').replace('октября', '10').replace('ноября', '11').replace('декабря', '12').replace('января', '01').replace('февраля', '02').replace('марта', '03').replace('апреля', '04').replace('мая', '05').replace('июня', '06').replace('июля', '07')
        current_date = record
        if len(record) == 4:
            current_date  = '0' + current_date
        if os.path.exists('C:/assistent_1/REMINDER_BY_DAY/'+ current_date +'.txt'):
            os.remove('REMINDER_BY_DAY/' + current_date + '.txt')
            ked.send("alt+f4")
            ked.send("enter")
            say_message('файл ' + current_date + ' удалён, что то ещё?')
        else: 
            say_message('такого файла не существует, задай другую дату')
    elif "выход" in message:
        exit()
        
def reminder_for_the_year():
    locale.setlocale(locale.LC_ALL, "ru")
    now = strftime("%A-%d-%m-%Y")
    say_message('напоминалка на сегодня '+now)
    nows = strftime("%d %m")
    print(nows)
    if os.path.exists('REMINDER_BY_DAY/'+ nows+'.txt'):
        f = open('REMINDER_BY_DAY/'+ nows +'.txt','r', encoding='utf-8')
        f_all = f.read()
        say_message(f_all)
        f.close()
    else:
        say_message('на сегодня напоминаний нет')

def say_message(message):

    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_" + \
    str(time.time())+"_"+str(random.randint(0, 100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Маруся: "+message)
  
if __name__ == '__main__':
    reminder_for_the_year()
    say_message('скажи запиши напоминалку когда спрошу на какой день скажи например двадцать седьмое августа')
   
    

    while True:
        
        command = listen_command()  # слушает команду
        do_tris_command(command)  # обрабатывает команду
        
      
