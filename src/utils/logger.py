import os
from datetime import datetime


class Logger:
    def __init__(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.file = open(path, "w")

    def log(self, msg):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{time}] {msg}"
        print(line)
        self.file.write(line + "\n")

    def close(self):
        self.file.close()