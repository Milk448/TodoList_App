class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def is_completed(self):
        return self.completed

    def mark_completed(self):
        self.completed = True
