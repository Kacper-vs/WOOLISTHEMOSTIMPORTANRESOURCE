import json
import os
import time
import configparser
import sys

from PUZZLES.puzzle1 import puzzle_1
from FUNCTIONS.typing_func import typing_print
from FUNCTIONS.typing_func import typing_input
from FUNCTIONS.typing_func import clear_screen

# VARIABLES
Y_OR_N = ["YES", "NO"]
C_OR_P = ["COURAGE", "PASSION"]


# ---------------------------
# INI COLOR SYSTEM
# ---------------------------
config = configparser.ConfigParser()

BASE_DIR = os.path.dirname(__file__)
INI_PATH = os.path.join(BASE_DIR, "ASSETS", "color.ini")

loaded = config.read(INI_PATH)


def get_prefix(section):
    return config[section]["prefix"]


def parse_ansi(value):
    return value.encode().decode("unicode_escape")


def get_color(section, key):
    return parse_ansi(config[section][key])


# Colors (safe load)
NARRATOR = get_color("narrator", "color")
WARNING = get_color("warning", "color")
SUCCESS = get_color("success", "color")
YOKAI = get_color("yokai", "color")

# RESET (always safe fallback)
RESET = "\033[0m"


def speak(prefix, color, text):
    typing_print(color + prefix + " " + text + RESET, 0.01)


def question(prefix, color, text):
    return typing_input(color + prefix + " " + text + RESET, 0.01)


# ---------------------------
# JSON PATHS
# ---------------------------
with open(
    os.path.join(BASE_DIR, "DIALOUGE", "dialouge_narrator.json"), "r", encoding="utf-8"
) as file:
    narrator_data = json.load(file)

with open(
    os.path.join(BASE_DIR, "DIALOUGE", "dialouge_entity.json"), "r", encoding="utf-8"
) as file:
    entity_data = json.load(file)


# ---------------------------
# DIALOGUE DATA
# ---------------------------
NARRATOR_WELCOME = narrator_data["NARRATOR_PRINT"]["WELCOME MESSAGE1"]
NARRATOR_PROMPT = narrator_data["NARRATOR_INPUT"]["PROMPT TO STRT MATCH"]

Yokai_greeting = entity_data["???"]["GREETING"]
Yokai_question1 = entity_data["???"]["QUESTION ONE"]


# ---------------------------
# GAME STORY
# ---------------------------
def story():
    speak(get_prefix("narrator"), NARRATOR, NARRATOR_WELCOME)

    time.sleep(0.5)

    prompt = question(get_prefix("narrator"), NARRATOR, NARRATOR_PROMPT)
    prompt = prompt.strip().upper()

    if prompt == Y_OR_N[0]:  # THIS REFERS TO YES
        clear_screen()
        speak(get_prefix("yokai"), YOKAI, Yokai_greeting)
        time.sleep(1)
        prompt2 = question(get_prefix("yokai"), YOKAI, Yokai_question1)
        if prompt2.strip().upper() == C_OR_P[0]:  # THIS REFERS TO COURAGE
            clear_screen()
            time.sleep(0.5)
            puzzle_1()

    elif prompt == Y_OR_N[1]:  # THIS REFERS TO NO
        clear_screen()
        typing_print(WARNING + "QUITTING... MISSION FAILED" + RESET, 0.05)
        sys.exit(0)

    else:
        clear_screen()
        typing_print(WARNING + "Invalid input..." + RESET, 0.05)

