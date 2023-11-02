import time
from random import uniform
from threading import Timer

from bot.logic import BotHandler
from share.logging import get_logger

class TienlenBot(object):
    MIN_TIME_DELAY = 1
    MAX_TIME_DELAY = 7
    MAX_PONG_DELAY = 20

    def __init__(self, bot_id: str, model_name: str, bot_type: int, handler: BotHandler):
        self.id = bot_id
        self.model_name = model_name
        self.bot_type = bot_type
        self.handler = handler
        self.logger = get_logger("bot " + bot_id)
