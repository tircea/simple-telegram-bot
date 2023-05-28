from lib import *

class Physics:
    def __init__(self, loaded_lang):
        self.state = None
        self.selected = None
        self.loaded_lang = loaded_lang
        self.ohmsArr = getLangText(self.loaded_lang, ["siltok", "naprag", "sopr"]) 
        self.energyConservArr = ["eken", "epot", "evn"]

    def solver(self, itemsArr, value , isOhms = False):
        state = "task"
        if not self.state:
            self.state = 1
            text, keyboard = askSelect(getLangText(self.loaded_lang, "what_find"), itemsArr)
            return text, keyboard, state
        
        if self.state == 1:
            self.selected = int(value)-1
            self.state = 2
            new_arr = itemsArr.copy()
            del new_arr[self.selected]
            return getLangText(self.loaded_lang, "you_find")+ itemsArr[self.selected]+"\n"+ getLangText(self.loaded_lang, "numss") + getLangText(self.loaded_lang, "and").join(new_arr), [], state
        
        if self.state == 2:
            try:
                [num1, num2] = arrFloat(value.split(" "))
                if self.selected == 0:
                    if not isOhms: 
                        result = num2-num1
                    else:
                        result = num1/num2
                elif self.selected == 1:
                    if not isOhms: 
                        result = num2-num1
                    else:
                        result = num1*num2
                elif self.selected == 2:
                    if not isOhms: 
                        result = num2+num1
                    else:
                        result = num2/num1
                return getLangText(self.loaded_lang, "your_nums") + f"{num1} {num2}, "+ getLangText(self.loaded_lang, "result") + f"{result}", [], "final"
            except:
                return getLangText(self.loaded_lang, "error_data"), [], state

    def energyConserv(self, value):
        return self.solver(self.energyConservArr, value)

    def ohmsLaw(self, value):
        return self.solver(self.ohmsArr, value, True)
