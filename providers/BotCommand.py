class BotCommand:
    def __init__(self, command: str, question: str, follow_up=None):
        self.command = command
        self.question = question
        self.follow_up = follow_up
