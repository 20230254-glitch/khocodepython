class Event:
    def __init__(self, date, text):
        self.date = date
        self.text = text

    def to_dict(self):
        return {
            "date": self.date,
            "text": self.text
        }