"""
Here, we wrap the original environment to make it easier
to use. When a game is finished, instead of mannualy reseting
the environment, we do it automatically.
"""
import numpy as np
import torch


from env.base.card import Card
from env.base.move import Move
from env.utils.utils import *


from app.dtos import HitCardReq


def strs2cards(list_cards: list[str]):
    return [Card(card) for card in list_cards]


def _one_hot_vector(signal: int, max_length: int, device):
    oh = [0] * (max_length + 1)
    oh[signal] = 1

    return torch.FloatTensor(oh).to(device)


def _cards2array(list_cards: list[Card]):
    """
    Convert a list of Card to List of int (one-hot format)
    """
    lst = [0] * 52

    for card in list_cards:
        card_shape = card.get_shape()
        card_type = card.get_type()
        if card.type == '2':
            card_type = 15

        card_type -= 3
        lst[card_type * 4 + card_shape] = 1

    return lst


def _cards2tensor(list_cards: list[str], device):
    """
    Convert a list of integers to the tensor
    representation
    """
    list_cards = strs2cards(list_cards)
    matrix = _cards2array(list_cards)
    matrix = torch.FloatTensor(matrix).to(device)
    return matrix


def _historical_actions2tensor(historical_actions: list[Move], device):
    """
    A utility function to encode the historical moves.
    We encode the historical 15 actions. If there is
    no 15 actions, we pad the features with 0. 
    Finally, we obtain a 15x52 matrix, which will be fed
    into LSTM for encoding.
    """
    matrix = []
    if historical_actions == None:
        historical_actions = []

    # print(historical_actions)
    if len(matrix)< 15:
        padding = [Move([]) for _ in range(15 - len(historical_actions))]
        historical_actions = padding + historical_actions
    for action in historical_actions[-15:]:
        matrix.append(_cards2array(action.move))
        if len(matrix) == 15:
            break

    return torch.FloatTensor(matrix).unsqueeze(0).to(device)


def _format_observation(req: HitCardReq, device):
    """
    A utility function to process observations and
    move them to CUDA.
    obs = {
        "position": infoset.player_position,

        "my_handcards": infoset.player_hand_cards,

        "other_hand_cards": infoset.other_hand_cards,

        "last_action": infoset.last_move,

        "1st_played_card": infoset.played_cards[(infoset.player_position + 1) % 4],
        "2nd_played_card": infoset.played_cards[(infoset.player_position + 2) % 4],
        "3rd_played_card": infoset.played_cards[(infoset.player_position + 3) % 4],

        "historical_action": infoset.card_play_action_seq
    }
    """

    if not device == "cpu":
        device = 'cuda:' + str(device)

    
    my_handcards = _cards2tensor(req.my_handcards, device)

    f_played_card = _cards2tensor(req.st_played_card, device)
    s_played_card = _cards2tensor(req.nd_played_card, device)
    t_played_card = _cards2tensor(req.rd_played_card, device)

    onehot_f_cards_left = _one_hot_vector(13 - len(req.st_played_card), 13, device)
    onehot_s_cards_left = _one_hot_vector(13 - len(req.nd_played_card), 13, device)
    onehot_t_cards_left = _one_hot_vector(13 - len(req.rd_played_card), 13, device)

    historical_action = _historical_actions2tensor(req.historical_action, device)
    
    
    x_batch = torch.FloatTensor(()).to(device)
    for action in req.legal_actions:

        # action = _cards2tensor(action.move, device=device)
        x_batch = torch.cat((x_batch, torch.hstack((
            _cards2tensor(action, device=device) if len(action) != 0 else torch.FloatTensor([-1] * 52).to(device),
            my_handcards,
            # union_other_handcards,
            # last_action,
            f_played_card,
            s_played_card,
            t_played_card,
            onehot_f_cards_left,
            onehot_s_cards_left,
            onehot_t_cards_left)).unsqueeze(0)),
            dim=0
        )

    # print(x_batch.shape)

    x_no_action = torch.hstack((
        my_handcards,
        # union_other_handcards,
        # last_action,
        f_played_card,
        s_played_card,
        t_played_card,
        onehot_f_cards_left,
        onehot_s_cards_left,
        onehot_t_cards_left,
    ))

    z = historical_action
    z_batch = z.repeat([len(req.legal_actions), 1, 1])

    obs = {
        'x_batch': x_batch,
        'z_batch': z_batch,
        'legal_actions': req.legal_actions,
    }
    return obs, x_no_action, z