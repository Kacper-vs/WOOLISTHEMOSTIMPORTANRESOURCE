import json
import os
import time
import configparser
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from FUNCTIONS.typing_func import typing_print
from FUNCTIONS.typing_func import typing_input
from FUNCTIONS.typing_func import clear_screen
from FUNCTIONS.typing_func import countdown_timer

# VARIABLES
Y_OR_N = ["YES", "NO"]
PZL_ANS = ["TULIP","ROOTS"]


config = configparser.ConfigParser()

SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INI_PATH = os.path.join(SRC_DIR, "ASSETS", "color.ini")
config.read(INI_PATH)

with open(
    os.path.join(SRC_DIR, "DIALOUGE", "dialouge_narrator.json"), "r", encoding="utf-8"
) as file:
    narrator_data = json.load(file)

with open(
    os.path.join(SRC_DIR, "DIALOUGE", "dialouge_entity.json"), "r", encoding="utf-8"
) as file:
    entity_data = json.load(file)


def get_prefix(section):
    return config[section]["prefix"]


def parse_ansi(value):
    return value.encode().decode("unicode_escape")


def get_color(section, key):
    return parse_ansi(config[section][key])


RESET = "\033[0m"
NARRATOR = get_color("narrator", "color")
WARNING = get_color("warning", "color")
SUCCESS = get_color("success", "color")
YOKAI = get_color("yokai", "color")

def speak(prefix, color, text):
    typing_print(color + prefix + " " + text + RESET, 0.01)


def question(prefix, color, text):
    return typing_input(color + prefix + " " + text + RESET, 0.01)

BEGINNING_PHRASE = entity_data["???"]["PUZZLE ONE"]
PHRASE_ONE = entity_data["pzl1_input"]["PHRASE ONE"]
PHRASE_TWO = entity_data["pzl1_input"]["PHRASE TWO"]
TAUNT = entity_data["???"]["TAUNT"]
NARRATOR_HINT = narrator_data["NARRATOR_PRINT"]["HINT_1"]

CHECK_AWNSER_1 = entity_data["YOKAI_CHECK"]["CHECK_AWNSER1"]
CHECK_AWNSER_2 = entity_data["YOKAI_CHECK"]["CHECK_AWNSER2"]

PRAISE_1 = entity_data["PRAISE"]["PRAISE_1"]
PRAISE_2 = entity_data["PRAISE"]["PRAISE_2"]

def puzzle_1():
    clear_screen()
    prompt = question(get_prefix("yokai"), YOKAI, BEGINNING_PHRASE)
    if prompt.strip().upper() == Y_OR_N[0]: # This refers to "YES"
        clear_screen()
        speak(get_prefix("yokai"), YOKAI, PHRASE_ONE)
        time.sleep(1)
        speak(get_prefix("yokai"), YOKAI, PHRASE_TWO)
        time.sleep(0.1)
        speak(get_prefix("yokai"), YOKAI, TAUNT)
        time.sleep(0.5)
        speak(get_prefix("narrator"), NARRATOR, NARRATOR_HINT)
        time.sleep(0.25)
        countdown_timer(30, YOKAI)
        clear_screen()
        CA1 = question(get_prefix("yokai"), YOKAI, CHECK_AWNSER_1)
        if CA1.strip().upper() == PZL_ANS[0]:
            CA2 = question(get_prefix("yokai"), YOKAI , CHECK_AWNSER_2)
            if CA2.strip().upper() == PZL_ANS[1]:
                speak(get_prefix("yokai"), YOKAI , PRAISE_2) #NEED TO ADD PRAISE 
                #TODO- PUZZLE 2 
                #PlaceHolderForPuzzle2
        
