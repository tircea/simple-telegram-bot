from lib import *
from datetime import datetime
import random

class General:
    def __init__(self, loaded_lang):
        self.loaded_lang = loaded_lang
        self.state = None
        self.questions = getLangText(loaded_lang, ['q1', 'q2', 'q3', 'q4', 'q5'])
        self.answers = []

    def year(self, value):
        result = datetime.now().year
        return getLangText(self.loaded_lang, "cur_year") + str(result), [], "final"

    def nyear(self, value):
        current_date = datetime.now().date()
        new_year = datetime(current_date.year + 1, 1, 1).date()
        result = (new_year - current_date).days
        return getLangText(self.loaded_lang, "n_year") + str(result), [], "final"

    def citat(self, value):
        citats = getLangText(self.loaded_lang, [
            "citat1",
            "citat2",
            "citat3",
            "citat4",
            "citat5"
        ])
        return random.choice(citats), [], "final"

    def illuminati(self, value):
        return getLangText(self.loaded_lang, "illuminati"), [], "final"

    def tiktok(self, value):
        return getLangText(self.loaded_lang, "tiktok"), [], "final"

    def arab(self, value):
        return getLangText(self.loaded_lang, "arab"), [], "final"

    def coin(self, value):
        return getLangText(self.loaded_lang, "coin"), [], "final"

    def million(self, value):
        return getLangText(self.loaded_lang, "work"), [], "final"

    def food(self, value):
        foodList = getLangText(self.loaded_lang, [
            "food1",
            "food2",
            "food3",
            "food4",
            "food5"
        ])
        return random.choice(foodList), [], "final"

    def game(self, value):
        templates = getLangText(self.loaded_lang, [
            "temp1",
            "temp2",
            "temp3",
            "temp4",
            "temp5"
        ])


        if self.questions == []:
            self.answers.append(value)
            story_template = random.choice(templates)
            story = story_template.format(*self.answers)
            return story, [], "final"
        
        question = self.questions.pop(0)
        if not self.state:
            self.state = 1
            return getLangText(self.loaded_lang, "give_answer") + question, [], "task"

        if self.state == 1:
            self.answers.append(value)
            return getLangText(self.loaded_lang, "give_answer") + question, [], "task"