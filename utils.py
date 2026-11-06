from colorama import Fore, Style, init

init(autoreset=True)

def heading(message):
    print(Fore.MAGENTA + Style.BRIGHT + "\n" + "=" * 58)
    print(f"{message:^58}")
    print("=" * 58 + Style.RESET_ALL)

def info(message):
    print(Fore.CYAN + str(message))

def good(message):
    print(Fore.GREEN + str(message))

def warn(message):
    print(Fore.YELLOW + str(message))

def bad(message):
    print(Fore.RED + str(message))

def ask(message):
    return input(Fore.WHITE + message + Style.RESET_ALL).strip()

def get_menu_choice(prompt, valid_choices):
    valid = {str(choice) for choice in valid_choices}
    while True:
        choice = ask(prompt)
        if choice in valid:
            return choice
        warn("Please enter one of these choices: " + ", ".join(sorted(valid)))
