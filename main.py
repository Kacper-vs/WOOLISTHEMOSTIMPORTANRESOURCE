import time
import random as rand
import sys
from input import clear_screen, print_slow, get_valid_input
from LOGIC import main_game

RED = "\033[0;31m"
GREEN = "\033[0;32m"
LIGHT_RED = "\033[1;31m"
BOLD = "\033[1m" 
END = "\033[0m"

uni_random = rand.uniform(0.08, 0.10)

def glitch_transition():
    clear_screen()
    glitch_chars = ["/", "-", "\\", "|", "#", "%", "@", "*"]
    
    for _ in range(3):
        sys.stdout.write(f"\r{RED}[ LOADING MEMORY BANKS... ]{END}")
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write(f"\r{LIGHT_RED}[ ERROR: NO IDENTITY FOUND ]{END}")
        sys.stdout.flush()
        time.sleep(0.15)
        
    clear_screen()
    time.sleep(0.5)

def official_starttothegame():
    time.sleep(1)
    print_slow("??? :", "ARE YOU WILLING TO BEGIN THIS EXPIDITION... (YES OR NO)", BOLD)
    
    choice = get_valid_input("> ", ["YES", "NO"])
    clear_screen()
    
    if choice == "YES":
        print_slow("SYSTEM:", "The expedition has commenced...", GREEN)
        time.sleep(1.5)
        glitch_transition()
        main_game()
    elif choice == "NO":
        print_slow("???:", "Then stay in the dark.", RED)
        time.sleep(2)
        clear_screen()
        sys.exit()

def main(timetoload):
    clear_screen()
    time.sleep(timetoload)
    
    print_slow("???:", "WeLcOmE tO ThE fLOWeR", RED)
    time.sleep(uni_random)
    
    print_slow("NARRATOR:", "FOR ANY CLUES FOLLOW TO www.theflowerdatabase.gg", LIGHT_RED)
    time.sleep(0.8)
    
    print_slow("???:", "Lets set a few house rules. You shall only awnser me in the terms [YES, NO] if not...", RED)
    time.sleep(0.4)
    print_slow("", "CoNsEqUeNcEs WiLl bE aPpLiEd.", RED)
    time.sleep(1.8)
    
    clear_screen()
    official_starttothegame()

if __name__ == "__main__":
    main(0.08)
