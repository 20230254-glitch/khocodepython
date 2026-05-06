import json
import os
from models.event import Event

FILE = "data/events.json"

def load_events():
    if not os.path.exists(FILE):
        os.makedirs("data", exist_ok=True)
        with open(FILE, "w") as f:
            json.dump([], f)

    with open(FILE, "r") as f:
        data = json.load(f)
        return [Event(e["date"], e["text"]) for e in data]

def save_events(events):
    with open(FILE, "w") as f:
        json.dump([e.to_dict() for e in events], f, indent=4)