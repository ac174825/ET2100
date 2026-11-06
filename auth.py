from database import create_account, check_login
from utils import ask, good, warn, bad, heading

def account_screen():
    heading("THE SHATTERED KINGDOM")
    print("STORY")
    print("For centuries, the Crystal of Dawn protected Eldoria.")
    print("The Shadow King shattered its magic and spread monsters across the land.")
    print("Find the three relics, help the people of Eldoria, and defeat the Shadow King.")
    print("Your choices and progress will be saved to your account.\n")

    while True:
        print("\n1. Register")
        print("2. Log in")
        print("3. Exit")
        choice = ask("Choose: ")

        if choice == "1":
            username = ask("Create username: ")
            password = ask("Create password: ")
            success, message = create_account(username, password)
            (good if success else warn)(message)
        elif choice == "2":
            username = ask("Username: ")
            password = ask("Password: ")
            success, message = check_login(username, password)
            if success:
                good(message)
                return username
            bad(message)
        elif choice == "3":
            return None
        else:
            warn("Please enter 1, 2, or 3.")
