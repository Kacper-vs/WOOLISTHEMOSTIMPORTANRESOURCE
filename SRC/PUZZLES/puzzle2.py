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

from FUNCTIONS.math_algorithim import gernerate_ez_problem 


#VARS # TEMP


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


WELLDONE = entity_data["PRAISE"]["WELLDONE"]





RESET = "\033[0m"
NARRATOR = get_color("narrator", "color")
WARNING = get_color("warning", "color")
SUCCESS = get_color("success", "color")
YOKAI = get_color("yokai", "color")

SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INI_PATH = os.path.join(SRC_DIR, "ASSETS", "color.ini")
config.read(INI_PATH)

def speak(prefix, color, text):
        typing_print(color + prefix + " " + text + RESET, 0.01)

def question(prefix, color, text):
    return typing_input(color + prefix + " " + text + RESET + 0.01)



def puzzle_2():
    clear_screen()
    time.sleep(0.25)
    speak(get_prefix("yokai"),YOKAI, WELLDONE)    #TEMP WELLDONE 
    gernerate_ez_problem()  
    #GIVE QUESTION BASED ON AWNSER 
    #MAKE USER HAVE 3 LIVES 
    #LOSE = DEATH 

puzzle_2()    
