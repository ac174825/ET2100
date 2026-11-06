from tinydb import TinyDB, Query
import hashlib
import os

DB_NAME = "game_data.json"
db = TinyDB(DB_NAME)
users = db.table("users")
User = Query()

def password_hash(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def create_account(username, password):
    username = username.strip()
    if len(username) < 3:
        return False, "Username must contain at least 3 characters."
    if len(password) < 4:
        return False, "Password must contain at least 4 characters."
    if users.contains(User.username == username):
        return False, "That username is already registered."
    users.insert({
        "username": username,
        "password_hash": password_hash(password),
        "progress": None
    })
    return True, "Account created. You can now log in."

def check_login(username, password):
    record = users.get(User.username == username.strip())
    if record is None or record["password_hash"] != password_hash(password):
        return False, "Incorrect username or password."
    return True, "Login successful."

def get_progress(username):
    record = users.get(User.username == username)
    if record is None:
        return None
    return record.get("progress")

def save_progress(username, player_data):
    users.update({"progress": player_data}, User.username == username)

def close_database():
    db.close()
