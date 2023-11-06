"""
This file includes the torch models. We use the same
model for 4 position in Tien Len.
"""

import numpy as np

import torch
from torch import nn

class LstmHitModel(nn.Module):
    def __init__(self, act_feature_size, state_feature_size,  hidden_size, num_layer):
        super().__init__()
        self.lstm_historical_move = nn.LSTM(52, hidden_size, batch_first=True, num_layers=num_layer)

        action_state_dim = act_feature_size + state_feature_size + hidden_size

        self.dense1 = nn.Linear(action_state_dim, 512)
        self.dense2 = nn.Linear(512, 512)
        self.dense3 = nn.Linear(512, 512)
        self.dense4 = nn.Linear(512, 512)
        self.dense5 = nn.Linear(512, 512)
        self.dense6 = nn.Linear(512, 512)
        self.dense7 = nn.Linear(512, 512)
        self.dense8 = nn.Linear(512, 512)
        self.dense9 = nn.Linear(512, 512)
        self.dense10 = nn.Linear(512, 512)
        self.dense11 = nn.Linear(512, 1)

    def forward(self, z, x, return_value=False, flags=None):
        c_n, (h_n, _) = self.lstm_historical_move(z)
        c_n = c_n[:,-1,:]
        x = torch.cat([c_n,x], dim=-1)

        x = self.dense1(x)
        x = torch.relu(x)
        x = self.dense2(x)
        x = torch.relu(x)
        x = self.dense3(x)
        x = torch.relu(x)
        x = self.dense4(x)
        x = torch.relu(x)
        x = self.dense5(x)
        x = torch.relu(x)
        x = self.dense6(x)
        x = torch.relu(x)
        x = self.dense7(x)
        x = torch.relu(x)
        x = self.dense8(x)
        x = torch.relu(x)
        x = self.dense9(x)
        x = torch.relu(x)
        x = self.dense10(x)
        x = torch.relu(x)
        x = self.dense11(x)
        if return_value:
            return dict(values=x)
        else:
            if flags is not None and flags.exp_epsilon > 0 and np.random.rand() < flags.exp_epsilon:
                action = torch.randint(x.shape[0], (1,))[0]
            else:
                action = torch.argmax(x,dim=0)[0]
            return dict(values=x, action=action)

    def init_weight(self, param_init= 0.1):
        for para in self.parameters():
            nn.init.uniform_(para, -param_init, param_init)