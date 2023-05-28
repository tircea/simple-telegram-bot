from lib import *
import math


class Mathematic:
    def __init__(self, loaded_lang):
        self.loaded_lang = loaded_lang

    def piNum(self, value):
        return getLangText(self.loaded_lang, "pi_num") + f"{math.pi}", [], "final"