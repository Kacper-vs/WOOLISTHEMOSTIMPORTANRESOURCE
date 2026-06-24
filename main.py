import sys
import time
import cmd

def print_slow(text, color_code):
    # Prints text smoothly with a retro color and resets it at the end
    sys.stdout.write(color_code)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\033[0m")

class BasicARG(cmd.Cmd):
    # Sets up the custom green retro terminal prompt
    prompt = "\033[1;32mUNKNOWN_NODE> \033[0m"

    def preloop(self):
        # This code runs automatically as soon as the game starts
        print_slow("--- SYSTEM REBOOT SUCCESSFUL ---", "\033[1;33m") # Yellow
        print_slow("Enter 'system_logs' to look for files...\n", "\033[0;36m") # Cyan

    def do_system_logs(self, arg):
        """Type this command to view the hidden system logs."""
        print_slow("LOG_01: Project Monarch initiated.", "\033[1;32m") # Green
        print_slow("LOG_02: Subject escaped into the grid.", "\033[1;31m") # Red

    def do_exit(self, arg):
        """Type 'exit' to close the terminal."""
        print_slow("Disconnecting...", "\033[1;31m")
        return True

if __name__ == "__main__":
    BasicARG().cmdloop()
