import requests
from telegram import Bot

bot = Bot(token='6193616106:AAGyXs34o-7iR1uuqdv3FFrc5OgCfWtW_j0')

URL = 'https://api.thecatapi.com/v1/images/search'

chat_id = 1284645597
response = requests.get(URL).json()

random_cat_url = response[0].get('url')

bot.send_photo(chat_id, random_cat_url)
