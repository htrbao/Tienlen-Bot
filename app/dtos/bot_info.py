from pydantic import BaseModel

from bot import TienlenBot


class BotInfo(BaseModel):
    namebot: str
    namemodel: str

    @staticmethod
    def create(bot: TienlenBot):
        return BotInfo(namebot=bot.id, namemodel=bot.model_name)
