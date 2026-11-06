from game import start
from database import close_database

if __name__ == "__main__":
    try:
        start()
    except (KeyboardInterrupt, EOFError):
        print("\nGame interrupted. If you want to preserve your latest progress, use Save and Quit.")
    finally:
        close_database()
