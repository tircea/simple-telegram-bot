def askSelect(usrText, arr, isTask=False, loaded_lang=False):
        x = 1
        key_i = 0
        text = ""
        keyboard = [[], [], [], [], []]
        for item in arr:
            if isTask:
                item = item[0]
            if loaded_lang:
                item = getLangText(loaded_lang, item)
            text = text + f"{x}. " + item + "\n"
            keyboard[key_i].append(f"{x}")
            if len(keyboard[key_i]) == 3:
                key_i = key_i + 1
            x = x + 1
        return usrText+"\n"+text, keyboard

def getLangText(loaded_lang, key):
        if type(key) == str:
            return loaded_lang[key.lower()]
        else:
            new = []
            for i in key:
                if type(i) != str:
                    new.append(getLangText(i))
                else: 
                    new.append(loaded_lang[i.lower()])
            return new

def arrFloat(arr):
    end = []
    for i in arr:
        end.append(float(i))
    return end