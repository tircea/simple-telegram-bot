from lib import *

import re
import collections

class Philology:
    def __init__(self, loaded_lang):
        self.state = None
        self.loaded_lang = loaded_lang

    def replaceAll(self, text, itemsList):
        for i in itemsList:
            text = text.replace(i, "")
        return text

    def fixText(self, text):
        return self.replaceAll(text, [",", ".", "!", "?", ")", "(", "@", "$", "^", "&"])

    def askForText(self):
        self.state = True
        return getLangText(self.loaded_lang, "send_text"), [], "task"

    def longest(self, value):
        if not self.state:
            return self.askForText()
        
        words = self.fixText(value).split()
        result = sorted(words, key=len, reverse=True)[:10]
        return getLangText(self.loaded_lang, "10long") + ", ".join(result), [], "final"

    def uniqWords(self, value):
        if not self.state:
            return self.askForText()
                
        words = self.fixText(value).split()
        unique_words = list(set(words))
        
        return getLangText(self.loaded_lang, "uniqwords") + ", ".join(unique_words), [], "final"

    def longestA(self, value):
        if not self.state:
            return self.askForText()

        words = re.findall(r'\b[йуеїіаоєяиюaeiouAEIOUЙУЕЇІАОЄЯИЮ]\w+', self.fixText(value))
        result = sorted(words, key=len, reverse=True)[:10]

        return getLangText(self.loaded_lang, "10long1") + ", ".join(result), [], "final"
    
    def letter(self, value):
        if not self.state:
            return self.askForText()
        
        letter_counts = collections.Counter(self.fixText(value).lower())
        result = letter_counts.most_common(1)[0][0] 

        return getLangText(self.loaded_lang, "commonlet") + result, [], "final"

    def longestB(self, value):
        if not self.state:
            return self.askForText()

        vowels = ['a', 'e', 'i', 'o', 'u', 'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']
        words = re.findall(r'\b\w+\b', value)
        result = [word for word in words if not any(vowel in word.lower() for vowel in vowels)]
        result = sorted(result, key=len, reverse=True)[:10]

        return getLangText(self.loaded_lang, "10long2") + ", ".join(result), [], "final"
        

    def palindromes(self, value):
        if not self.state:
            return self.askForText()
                
        words = self.fixText(value).split()
        result = [word for word in [word for word in words if word.lower() == word.lower()[::-1]] if len(word) >= 3]
        return getLangText(self.loaded_lang, "palindrom") + ", ".join(result), [], "final"