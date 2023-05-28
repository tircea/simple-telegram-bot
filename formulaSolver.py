from lib import *

import math

class Solver:
    def __init__(self, loaded_lang, taskData, taskName):
        self.loaded_lang = loaded_lang
        self.taskData = taskData
        self.taskName = taskName
        self.state = None

    def solve(self, value):
        [name, formula, varCount] = self.taskData
        numsData = {}
        if not self.state:
            self.state = 1
            return getLangText(self.loaded_lang, "you_find") + f"{getLangText(self.loaded_lang,self.taskName)} ({formula})\n" + getLangText(self.loaded_lang, "numss2"), [], "task"

        try:
            numsArr = arrFloat(value.split(" "))
            i = 1
            for item in numsArr:
                exec(f"n{i}={item}")
                i = i+1
            result = eval(formula)
            joinedNums = ", ".join(map(str, numsArr))
            return getLangText(self.loaded_lang, "your_nums") + f"{joinedNums}\n" + getLangText(self.loaded_lang, "formula_calc") + f" {name} = {formula}\n\n{name} = {result}", [], "final"
        except:
            return getLangText(self.loaded_lang, "error_data"), [], "task"
