"""Телеграмм бот. Ловец сновидений. Минимальная рабочая версия."""
import logging
import os

import speech_recognition as sr
import telegram
from pydub import AudioSegment
from serpapi import GoogleSearch
from telegram import Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)

from exceptions import SendMessageError
from settings import GOOGLE_TOKEN, TELEGRAM_TOKEN

logging.basicConfig(
    format='%(asctime)s | %(name)s | %(levelname)s | '
           '%(funcName)s | %(message)s',
    level=logging.DEBUG,
)


def send_message(bot, chat_id, message):
    """Отправляет сообщения в чат."""
    try:
        bot.send_message(chat_id, message)
    except telegram.error.TelegramError as e:
        logging.exception(f'Ошибка отправки сообщения: `{e}`')
        raise SendMessageError(e) from e


def send_photo(bot, chat_id, image, caption):
    """Отправляет сообщения в чат."""
    try:
        bot.send_photo(
            chat_id,
            image,
            caption=f'Сновидение поймано:\n {caption}',
        )
    except telegram.error.TelegramError as e:
        logging.exception(f'Ошибка отправки сообщения: `{e}`')
        raise SendMessageError(e) from e


def get_image(query):
    """Получаем изображение из текста сновидения."""
    search = GoogleSearch(
        {
            "q": query,
            "localization": "google_domain",
            "tbm": "isch",
            "ijn": "0",
            "device": "mobile",
            "api_key": GOOGLE_TOKEN
        }
    )
    result = search.get_dict()

    lighthouse_photo = result.get('images_results')[0].get('original')

    return lighthouse_photo


def write_text(update: Update, context: CallbackContext):
    """Обработчик введенного вручную текста."""
    lighthouse = get_image(update.message.text)
    chat = update.effective_chat
    send_photo(context.bot, chat.id, lighthouse, caption=update.message.text)


def say_voice(update: Update, context: CallbackContext):
    """
    Обработчик голосового ввода.

    Преобразует его текст. Ищет маячок сновидения и прикрепляет его к нему.
    Использует:
        -`google serpapi` для поиска, и сервис google для перевода голоса.
    """
    chat = update.effective_chat
    file_id = update.message.voice.file_id
    audio_tg = context.bot.get_file(file_id=file_id)
    audio_tg.download('captured.ogg')

    ogg_version = AudioSegment.from_ogg('captured.ogg')
    ogg_version.export('output.wav', format="wav")

    r = sr.Recognizer()
    with sr.AudioFile('output.wav') as source:
        audio = r.record(source)

    text_dream = ''
    try:
        text_dream = r.recognize_google(audio, language='ru-RU')
        logging.info(f'Голос преобразован: `{text_dream}`')
    except sr.UnknownValueError:
        logging.error(
            "Google Speech Recognition could not understand audio"
        )
    except sr.RequestError as e:
        logging.error(
            "Could not request results from Google Speech Recognition "
            "service; {0}".format(e))

    lighthouse = get_image(text_dream)
    send_photo(context.bot, chat.id, lighthouse, caption=text_dream)


def wake_up(update: Update, context: CallbackContext):
    """Обработчик кнопки '/start'."""
    chat = update.effective_chat
    msg = ('Ловец снов активирован ...'
           '\nв момент пробуждения, запиши голосовое. Опиши что видел.')
    send_message(context.bot, chat.id, msg)


def main():  # noqa: C901
    """Основная логика работы бота."""
    updater = Updater(token=TELEGRAM_TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.voice, say_voice))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, write_text))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print('\nStarting https://t.me/my_dreamcatcher_bot'
          '\n(Quit the bot with CONTROL-C.)')
    try:
        main()
    except KeyboardInterrupt:
        print('\nShutdown dreamcatcher ...')
        os._exit(0)
