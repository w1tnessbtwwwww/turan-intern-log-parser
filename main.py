from app.settings.settings import settings
import os
import telebot

# Замените на ваш токен и chat_id
TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN
CHAT_ID = settings.CHAT_ID
LOG_FILE_PATH = "logs/laravel.log"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def send_message_to_telegram(message):
    bot.send_message(CHAT_ID, message)

def process_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if (len(lines) % 174 == 0):
            send_message_to_telegram(lines[-1])

if __name__ == "__main__":
    process_log_file(LOG_FILE_PATH)
