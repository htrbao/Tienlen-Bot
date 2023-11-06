import os
import torch

from bot.logic.dmc.model import LstmHitModel
from bot.logic import BotHandler

class DMCHandler(BotHandler):
    def __init__(self, device):
        super().__init__(device)
        self.model = LstmHitModel(act_feature_size=52, 
                         state_feature_size=250, 
                         hidden_size=128, 
                         num_layer=1)
        # pretrained = torch.load('/Users/lap60754/Documents/vain/Tien-Len-Mien-Nam/TLMN/bot/sl/masterlog_checkpoints/master_31.pt', map_location='cpu')
        pretrained = torch.load(os.path.join('bot/logic/dmc/model/', 'model.pt'), map_location=device)

        self.model.load_state_dict(pretrained['model_state_dict'])
        if torch.cuda.is_available():
            self.model.cuda()

    def start_game(self):
        pass

    def handle_hit_card(self, obs: dict):
        with torch.no_grad():
            agent_output = self.model(obs['z_batch'], obs['x_batch'])
            _action_idx = int(agent_output['action'].cpu().detach().numpy())

            return _action_idx