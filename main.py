import requests

from pprint import pprint
import time

import random

URL = 'https://api.telegram.org/bot'
TOKEN = "ТОКЕН"

words = "ёлка  иголка зелёнка стоит светит торчит"
words = words.split()

offset = 0
while True:
    response = requests.get(URL + TOKEN + "/getUpdates?offset=" + str(offset))
    updates = response.json()['result']
    pprint(updates)
    if updates != []:
        requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={"составь стишок из слов: ёлка  иголка зелёнка стоит светит торчит"}')
        # Обработайте каждое обновление
        for update in updates:
            offset = update['update_id'] + 1
            pprint(updates)
            message = updates[-1]['message']
            chat_id = message['chat']['id']
            text = message['text']

            # Сделать проверку рифмованного текста
            text = text.split()

            for word in text:
                if word not in words:
                    requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={"ТЫ ИСПОЛЬЗОВАЛ СЛОВА КОТОРЫХ НЕ БЫЛО В ЗАДАНИИ"}')
                    break
            else:
                if text[1][-1:-3:-1] == text[3][-1:-3:-1]:
                    requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={"https://poiskpodarkov.com/wp-content/uploads/2017/07/risunok-k-prazdniku.jpg"}')
    else:
        # Если нет новых обновлений, вы можете добавить задержку перед следующим запросом, чтобы не нагружать сервер
        print("Обновлений нету!", updates)
        time.sleep(2)
