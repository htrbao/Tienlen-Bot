import torch


from bot import TienlenBot, TienlenBotFactory, _format_observation
from app.dtos import HitCardReq


class BotPool:
    def __init__(self, accounts, bot_types: list[int] = [0, 1]):
        self.accounts = accounts
        self.bots: dict[int, TienlenBot] = {}
        self.device: str = 'cuda' if torch.cuda.is_available() else 'cpu'
        for i in bot_types:
            self.create_bot(i)

    def create_bot(self, bot_type: int):
        for bot_t in self.bots.keys():
            if bot_type == self.bots[bot_t].bot_type:
                return bot
            
        bot = None
        for account in self.accounts:
            if account["bot_type"] == bot_type: 
                bot = TienlenBotFactory.create_bot(account["name"], account["real"], account["bot_type"], self.device)
                if bot is not None:
                    self.bots[account["bot_type"]] = bot
                    return True

        return None

    def predict_action(self, req: HitCardReq):
        obs, _, _ = _format_observation(req, self.device)
        action_idx = self.bots[req.bot_type].handler.handle_hit_card(obs)
        return obs['legal_actions'][action_idx]