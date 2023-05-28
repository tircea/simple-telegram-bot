# Simple Telegram Bot

This is a multilingual and extensible telegram bot written in Python 3. It is designed to be easily configurable and adaptable to a variety of use cases.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure that you have Python3 installed on your machine.

### Installation

Clone the repository

```bash
git clone https://github.com/tircea/simple-telegram-bot.git
cd simple-telegram-bot
```
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

## Configuration

Create a config.json file in the root directory of the project and specify the telegram bot token in the following format:

```json
{
    "telegram_token": "token_telegram_bot"
}
```

You can get a token for a Telegram bot by creating a new bot through BotFather in Telegram. 
Instructions on how to create a new bot can be found [here](https://core.telegram.org/bots#6-botfather).

For multilingual support, add the desired language to the langs.json file and create a new lang_{lang}.json file where you specify the keys and their corresponding translations.

## Adding Functionality

You can add your own functionality to the bot by editing the categories.json file.

The format is as follows:

```json

{
    "Physics": [
        ["ohmslaw", "ohmsLaw", false],
        ["lawenergy", "energyConserv", false],
        ["coulomblaw", ["F", "n1 * (n2 * n3) / n4 ** 2", 4], true],
        ...
    ],
    "Geography": [
        ["lang_key", "solveFunc", false],
        ...
    ],
    "Mathematic": [
        ...
    ]
}
```

Each key is a category and the arrays inside are the questions related to that category.

- The first value in the array is the language key by which the translation is retrieved from the file.
- The second value in the array is the solution function, or the formula to be solved.
- The third value is a boolean. It is set to true if the second value in the array is a formula that needs to be calculated. If the value is false, then the second value is a function that needs to be called.

In order to add functionality for a function from categories.json, create a new python file with a class whose names are equal to the names of the keys.

Here is an example of how the class should be structured:

```python

class Geography:
    def __init__(self, loaded_lang):
        self.loaded_lang = loaded_lang
        
   def solveFunc(self, value):
        return getLangText(self.loaded_lang, "lang_key"), [], "final" # First value is message, second is keyboard to return, last is bot state, if we done with solving we can return "final", if we need some additional data from user we can return "task"
```
## Usage

Once you have everything set up and configured, run the bot:

```bash
python3 main.py
```
