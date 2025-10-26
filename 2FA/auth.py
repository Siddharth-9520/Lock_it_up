# auth.py
from config import USERS

def authenticate_user(username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False
