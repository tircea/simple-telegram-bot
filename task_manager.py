from physics import Physics
from mathematic import Mathematic
from geography import Geography
from philology import Philology
from general import General

from lib import *
from formulaSolver import Solver


import json
import sys
import importlib


class TaskManager:
    def __init__(self, topics, loaded_lang, topicsTasks, category):
        self.topics = topics
        self.topicsTasks = topicsTasks
        self.loaded_lang = loaded_lang

        categoryName = topics[int(category)-1]
        categoryClass = getattr(sys.modules[__name__], categoryName)
        
        self.category = categoryName
        self.categoryClass = categoryClass(self.loaded_lang)
        self.taskConfig = None
        self.currentTask = None
        self.solver = None

    def getTasks(self):
        try:
            self.taskConfig = self.topicsTasks[self.category]
            return self.taskConfig
        except:
            return False

    def printTasks(self, tasks):
        x = 1
        text = ""
        keyboard = []
        for [task, taskFunc] in tasks:
            text = text + f"{x}. " + getLangText(self.loaded_lang, task) + "\n"
            keyboard.append(f"{x}")
            x = x + 1
        return text, keyboard

    def load_tasks(self):
        tasksData = self.getTasks()
        if not tasksData:
            return "ERROR!", [], "error"
        
        text, keyboard = askSelect(getLangText(self.loaded_lang, "task_select"), tasksData, True, self.loaded_lang)
        return text, keyboard, "task"

    def calculateTask(self, task):
        if not self.currentTask:
            self.currentTask = int(task)
        try:
            isFormula = self.taskConfig[self.currentTask-1][2]
            taskFunc = self.taskConfig[self.currentTask-1][1]
            if not isFormula:
                return getattr(self.categoryClass, taskFunc)(task)
            else:
                if not self.solver:
                    solver = Solver(self.loaded_lang, taskFunc, self.taskConfig[self.currentTask-1][0])
                    self.solver = solver
                    return solver.solve(task)
                else:
                    return self.solver.solve(task)
        except:
            return "ERROR!", [], "error"
