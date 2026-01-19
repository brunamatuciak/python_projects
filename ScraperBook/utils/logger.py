from datetime import datetime

def info(message):
    print(f"[{datetime.now()}] INFO: {message}")

def error(message):
    print(f"[{datetime.now()}] ERROR: {message}")
