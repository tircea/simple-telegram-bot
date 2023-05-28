from task_manager import TaskManager
import json

from lib import *


class DialogueManager:
    def __init__(self, topics, topicsTasks, langConfig):
        self.topics = topics
        self.topicsTasks = topicsTasks
        self.langConfig = langConfig
        self.language = None
        self.current_state = None
        self.current_task = None
        self.loaded_lang = None
        self.current_category = None

    def get_text(self, key):
        if type(key) == str:
            return self.loaded_lang[key.lower()]
        else:
            new = []
            for i in key:
                if type(i) != str:
                    new.append(self.get_text(i))
                else: 
                    new.append(self.loaded_lang[i.lower()])
            return new

    def set_language(self, language):
        self.language = language
        with open(f"lang_{language}.json", 'rb') as lang_file:
            self.loaded_lang = json.load(lang_file)
    
    def stepBack(self):
        self.current_state = "category"
        return self.choose_category()


    def get_response(self, message):
        languages = self.langConfig
        try:
            if not self.language:
                lang_key = languages[message]
                self.set_language(lang_key)
                self.current_state = "category"
                return self.choose_category()

            if self.current_state is None:
                data = self.choose_category()
                self.current_state = "category"
                return data

            if self.current_state == "category":
                data = self.choose_task(message)
                self.current_state = "task"
                return data

            if self.current_state == "task":
                text, keyboard, state = self.current_task.calculateTask(message)
                if state == "final":
                    self.current_state = "category"
                    return askSelect(text + "\n\n" + self.get_text("cat_select")+":", self.get_text(self.topics))

                if state == "error":
                    text, keyboard = self.choose_task(self.current_category)
                    text = self.get_text("error_key")+"\n\n" + text
                    state = "task"
                self.current_state = state
                return text, keyboard
        except:
            if not self.language:
                return "Error! Click on buttons from chat keyboard!", []
            else:
                return getLangText(self.loaded_lang, "error_key"), []

    def choose_category(self):
        return askSelect(self.get_text("cat_select")+":", self.get_text(self.topics))

    def choose_task(self, category):
        task_manager = TaskManager(self.topics, self.loaded_lang, self.topicsTasks, category)
        text, keyboard, state = task_manager.load_tasks()
        self.current_category = category
        self.current_state = state
        self.current_task = task_manager
        return text, keyboard