from lib import *

class Geography:
    def __init__(self, loaded_lang):
        self.loaded_lang = loaded_lang

    def materic(self, value):
        return getLangText(self.loaded_lang, "big_materic"), [], "final"

    def city(self, value):
        return getLangText(self.loaded_lang, "big_city"), [], "final"

    def vodohran(self, value):
        return getLangText(self.loaded_lang, "2_country"), [], "final"