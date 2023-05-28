from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import logging
import json
from datetime import datetime
from lib import *

from singleton import Singleton
from dialogue_manager import DialogueManager


class Bot(Singleton):
    def __init__(self, token: str):
        self.updater = Updater(token)
        self.dp = self.updater.dispatcher
        with open("categories.json", 'rb') as topics:
            data = json.load(topics)
            self.topics = list(data.keys())
            self.topicsTasks = data

        self.dialogue_managers = {}
        with open("langs.json", 'rb') as languages:
            data = json.load(languages)
            self.langConfig = data
            self.languages = list(map(lambda x: [x], list(data.keys())))

        self.dp.add_handler(CommandHandler("start", self.start))
        self.dp.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))
        
        current_date = datetime.now().strftime('%Y-%m-%d')
        logging.basicConfig(
            filename=f'log_{current_date}.log',
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO,
        )

        self.logger = logging.getLogger(__name__)

    def get_dialogue_manager(self, user_id):
        if user_id not in self.dialogue_managers:
            self.dialogue_managers[user_id] = DialogueManager(self.topics, self.topicsTasks, self.langConfig)

        return self.dialogue_managers[user_id]

    def clear_dialogue_manager(self, user_id):
        if user_id in self.dialogue_managers:
            del self.dialogue_managers[user_id]
        return None

    def start(self, update: Update, context: CallbackContext) -> None:
        user_id = update.message.chat_id
        dialogue_manager = self.get_dialogue_manager(user_id)
        if dialogue_manager:
            self.clear_dialogue_manager(user_id)
        update.message.reply_text(
            "Choose your language / Оберіть мову",
            reply_markup=ReplyKeyboardMarkup(self.languages, one_time_keyboard=True),
        )

    def echo(self, update: Update, context: CallbackContext) -> None:
        user_id = update.message.chat_id
        logging.info(f"[UserMessage] UserId: {user_id}, message: {update.message.text}")
        dialogue_manager = self.get_dialogue_manager(user_id)
        if update.message.text == "BACK":
            response, keyboard = dialogue_manager.stepBack()
        else:
            response, keyboard = dialogue_manager.get_response(update.message.text)
            logging.info(f"[BotMessage] UserId: {user_id}, message: {response}")
        if keyboard != []:
            keyboard.append(["BACK"])

        update.message.reply_text(response, 
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))

    def run(self):
        self.updater.start_polling()
        self.updater.idle()


if __name__ == "__main__":
    with open("config.json") as config_file:
        config = json.load(config_file)

    bot = Bot(config["telegram_token"])
    bot.run()