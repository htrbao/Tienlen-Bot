from bot import TienlenBot
from bot.logic import BotHandler, DMCHandler, SLHandler


class TienlenBotFactory:
    @staticmethod
    def create_bot(bot_id: str, bot_real: str, bot_type: int, device: str):
        if bot_type == 0:
            return TienlenBot(bot_id, bot_real, bot_type, DMCHandler(device))
        elif bot_type == 1:
            return TienlenBot(bot_id, bot_real, bot_type, SLHandler(device))
        else :
            return None
