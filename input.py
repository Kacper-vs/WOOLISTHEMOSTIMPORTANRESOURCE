import os
import sys
import time

BOLD = "\033[1m"
RED = "\033[0;31m"
END = "\033[0m"

if os.name == 'nt':
    import msvcrt
else:
    import select

def get_timed_input(prompt, seconds_limit):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    
    input_buffer = ""
    start_time = time.time()
    time_left = seconds_limit

    while time_left > 0:
        elapsed = time.time() - start_time
        time_left = max(0, int(seconds_limit - elapsed))
        
        sys.stdout.write(f"\r{prompt} [{RED}{time_left}s remaining{END}] > {input_buffer}")
        sys.stdout.flush()

        if os.name == 'nt':
            if msvcrt.kbhit():
                char = msvcrt.getwche()
                if char in ('\r', '\n'):
                    print()
                    return input_buffer.strip().upper()
                elif char == '\b':
                    if len(input_buffer) > 0:
                        input_buffer = input_buffer[:-1]
                        sys.stdout.write("\b \b")
                else:
                    input_buffer += char
        else:
            rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
            if rlist:
                char = sys.stdin.read(1)
                if char in ('\r', '\n'):
                    return input_buffer.strip().upper()
                elif char in ('\x7f', '\b'):
                    if len(input_buffer) > 0:
                        input_buffer = input_buffer[:-1]
                else:
                    input_buffer += char
                    
        time.sleep(0.05)

    print("\n")
    return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(prefix, text, color_code):
    full_text = f"{prefix} {text}" if prefix else text
    sys.stdout.write(color_code)
    for char in full_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\033[0m") 

def get_valid_input(prompt, valid_choices):
    while True:
        user_choice = input(f"{BOLD}{prompt}{END} ").strip().upper()
        
        if user_choice in valid_choices:
            return user_choice
        
        clear_screen()
        print_slow("???:", "INVALID ANSWER. PAY ATTENTION TO THE RULES.", RED)
        time.sleep(1)
