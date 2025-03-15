import json
import os

class UserManager:
    def __init__(self, filename="user_data.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({"preferences": [], "history": []}, f)

    def load_data(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def add_preference(self, topic):
        data = self.load_data()
        if topic not in data["preferences"]:
            data["preferences"].append(topic)
        self.save_data(data)

    def get_preferences(self):
        return self.load_data().get("preferences", [])

    def add_history(self, search):
        data = self.load_data()
        data["history"].append(search)
        self.save_data(data)

    def get_history(self):
        return self.load_data().get("history", [])
