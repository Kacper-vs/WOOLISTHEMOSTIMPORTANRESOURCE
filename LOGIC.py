import time
import sys
from input import clear_screen, print_slow, get_valid_input, get_timed_input

RED = "\033[0;31m"
GREEN = "\033[0;32m"
LIGHT_RED = "\033[1;31m"
BOLD = "\033[1m" 
ITALIC = "\033[3m"
END = "\033[0m"

PUZZLE_1 = [
    'The Underground Life Is Perfect', 
    'Radiant Owls Often Travel Silent'
]

def fail_sequence(reason):
    clear_screen()
    if reason == "TIMEOUT":
        print_slow("Satyr :", "TICK TOCK. TIME IS UP.", RED)
    else:
        print_slow("Satyr :", "WRONG. You completely misread the patterns.", RED)
    
    time.sleep(1.5)
    print_slow("SYSTEM :", "Expedition terminated. Consequences applied.", RED)
    time.sleep(2)
    sys.exit()

def first_puzzle():
    clear_screen()
    print_slow("??? :", "Would you like to get to know me...?", LIGHT_RED)
    time.sleep(0.5)
    
    choice = get_valid_input(">", ["YES", "NO"])
    clear_screen()
    
    if choice == "YES":
        print_slow("Satyr :", "So now that you know my name...", LIGHT_RED)
        time.sleep(0.5)
        print_slow("Satyr :", "Are you STILL willing to continue?", LIGHT_RED)
        time.sleep(0.5)
        
        choice = get_valid_input(">", ["YES", "NO"])
        clear_screen()
        
        if choice == "YES":
            print_slow("Satyr :", "Well then. Here are your phrases. Do what you must.", GREEN)
            time.sleep(1.5)
            clear_screen()
            
            for riddles in PUZZLE_1:
                print_slow("Satyr :", f"\"{riddles}\"", RED)
                time.sleep(0.8)
                
            time.sleep(1.5)
            print_slow("\nNARRATOR :", "Capitals are where the answer lies...", BOLD + ITALIC)
            time.sleep(1)
            print_slow("\nNARRATOR :", "You have 20 seconds to awnser this...", BOLD + ITALIC)
            get_timed_input("TIME_TO_SOLVE", seconds_limit=20); time.sleep(20)
            clear_screen()
            
            print_slow("Satyr :", "Decode phrase 1 instantly...", LIGHT_RED)
            answer_1 = get_timed_input("DECODE 1", seconds_limit=10)
            
            if answer_1 is None:
                fail_sequence("TIMEOUT")
            elif answer_1 != "TULIP":
                fail_sequence("WRONG")
                
            clear_screen()
            print_slow("Satyr :", "Correct. Now decode phrase 2 before the clock stops...", GREEN)
            time.sleep(1)
            answer_2 = get_timed_input("DECODE 2", seconds_limit=10)
            
            if answer_2 is None:
                fail_sequence("TIMEOUT")
            elif answer_2 != "ROOTS":
                fail_sequence("WRONG")
            
            clear_screen()
            print_slow("Satyr :", "Impressive. You successfully passed the gates of TULIP and ROOTS.", GREEN)
            time.sleep(2)
            
    elif choice == "NO":
        print_slow("Satyr :", "Ignorance is bliss, isn't it?", RED)
        time.sleep(2)
        sys.exit()

def main_game():
    print_slow("??? :", "Will you tell me what it is you seek?", LIGHT_RED)
    print_slow("??? :", f"[{BOLD}COURAGE{END}{LIGHT_RED}] OR [{BOLD}PASSION{END}{LIGHT_RED}].", LIGHT_RED)
    
    choice = get_valid_input(">", ["COURAGE", "PASSION"])
    clear_screen()
    
    if choice == "COURAGE":
        print_slow("??? :", "So be it...", RED)
        time.sleep(1)
        first_puzzle()
    elif choice == "PASSION":
        print_slow("??? :", "May your choice twist your future...", GREEN)
        time.sleep(1)
        first_puzzle()
