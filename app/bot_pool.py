from bot import TienlenBot, TienlenBotFactory


class BotPool:
    def __init__(self, accounts):
        self.accounts = accounts
        self.bots: list[TienlenBot] = []

    def create_bot(self, bot_type: int):
        for bot in self.bots:
            if bot_type == bot.bot_type:
                return bot
            
        bot = None
        for account in self.accounts:
            if account["bot_type"] == bot_type: 
                bot = TienlenBotFactory.create_bot(account["name"], account["real"], account["bot_type"])
                if bot is not None:
                    self.bots.append(bot)
                    return bot

        return None

    def is_have_bot_in_room(self) -> bool:
        return (len(self.bots) > 0)

    def handle_bot_leave_room(self, bot_type: int):
        for i in range(len(self.bots)):
            if self.bots[i].bot_type == bot_type:
                self.bots.pop(i)

