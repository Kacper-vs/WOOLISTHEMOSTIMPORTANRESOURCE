import json 
import os 
import time 
import configparser 
import sys 

# Ensure the path is set up correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from FUNCTIONS.typing_func import typing_print
from FUNCTIONS.typing_func import typing_input
from FUNCTIONS.typing_func import clear_screen
from FUNCTIONS.typing_func import countdown_timer 

# --- CONFIGURATION & GLOBALS ---

config = configparser.ConfigParser()
SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INI_PATH = os.path.join(SRC_DIR, "ASSETS", "color.ini")

# Read config once at the start
config.read(INI_PATH)

# Load JSON data
with open(os.path.join(SRC_DIR, "DIALOUGE", "dialouge_narrator.json"), "r", encoding="utf-8") as file:
    narrator_data = json.load(file)

with open(os.path.join(SRC_DIR, "DIALOUGE", "dialouge_entity.json"), "r", encoding="utf-8") as file:
    entity_data = json.load(file)

# --- HELPER FUNCTIONS ---

def get_prefix(section):
    return config[section]["prefix"]

def parse_ansi(value):
    # Handles escape sequences safely
    try:
        return value.encode().decode("unicode_escape")
    except UnicodeDecodeError:
        return value

def get_color(section, key):
    raw_val = config[section].get(key, "")
    return parse_ansi(raw_val)

def speak(prefix, color, text):
    typing_print(color + prefix + " " + text + "\033[0m", 0.01)

def question(prefix, color, text):
    return typing_input(color + prefix + " " + text + "\033[0m", 0.01)

# --- GAME STATE ---

lives = 3 

# Constants from JSON
MATHQUESTIONPROMPT = entity_data["pzl2_input"]["PROMPT1"]
WELLDONE_TEXT = entity_data["PRAISE"]["WELLDONE"]
LOSELIVE_TAUNT = entity_data["MAIN_TAUNT"]["LOSELIVEPROMPT"]
PZL2_HINT = narrator_data["NARRATORHINT"]["PUZZLE2_HINT"]


# Color Constants
RESET = "\033[0m"
NARRATOR = get_color("narrator", "color")
WARNING = get_color("warning", "color")
SUCCESS = get_color("success", "color")
YOKAI = get_color("yokai", "color")

# --- LOGIC FUNCTIONS ---

def mathproblema():
    x = 10 
    z = 21 
    y = 10 
    soulution = x + y * z
    speak(get_prefix('yokai'), YOKAI , f"Consider this your second puzzle... What's {x} + {y} * {z}")
    raw_prompt = question(get_prefix('yokai'), YOKAI , )
    prompt = raw_prompt.strip().upper()
    if prompt == str(solution):
        print('well done ')

def lose_live(amount):
    global lives
    lives = lives - amount
    # Ensure lives don't go below 0 for display purposes
    display_lives = max(0, lives)
    speak(get_prefix('yokai'), YOKAI, f"You have {display_lives} lives remaining")

def puzzle_2():
    clear_screen()
    time.sleep(0.25)
    
    # Speak the praise message
    speak(get_prefix("yokai"), YOKAI, WELLDONE_TEXT)
    speak(get_prefix('narrator'), NARRATOR, PZL2_HINT)
    # Get input
    raw_input = question(get_prefix('yokai'), YOKAI, MATHQUESTIONPROMPT)
    
    # CRITICAL FIX: Normalize input immediately
    # .strip() removes accidental spaces, .upper() makes it case-insensitive
    prompt = raw_input.strip().upper()

    if prompt == "YES":
        speak(get_prefix('yokai'), YOKAI, "CORRECT. [INSERT EASY QUESTION HERE]")
        
        # Example: lives = 3
        
    elif prompt == "NO":
        speak(get_prefix('yokai'), YOKAI, "CORRECT, INSERT HARD QUESTION HERE")
        
    else:
        # Handle invalid input
        speak(get_prefix('warning'), WARNING, "Invalid input. Please type 'YES' or 'NO'.")
        time.sleep(1)
        # Recursively call the function to retry, or loop in a game engine
        puzzle_2()

    # Optional: Check if player died from previous logic (not implemented in this snippet)
    if lives <= 0:
        speak(get_prefix('warning'), WARNING, "GAME OVER")
        sys.exit()

# --- EXECUTION ---

if __name__ == "__main__":
    puzzle_2()