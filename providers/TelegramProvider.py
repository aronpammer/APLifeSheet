import telegram


class TelegramProvider:
    def __init__(self, token: str):
        self.token = token
        self.bot = telegram.Bot(token=token)

    def send_message(self):
        pass
