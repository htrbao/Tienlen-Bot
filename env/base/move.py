from copy import deepcopy
import collections

from env.base import Card
from env.utils.utils import *

class Move:
    def __init__(self, move) -> None:
        self.move : list[Card] = []
        
        self.type : int = None

        for card in move:
            if isinstance(card, int):
                self.move.append(Card(card))
            else:
                self.move.append(card)

        self.move.sort(key=lambda x: x.id)

        self.get_move_type()

    def is_continuous_seq(self):
        for i in range(len(self.move) - 1):
            if self.move[i + 1].get_type() - self.move[i].get_type() != 1:
                return False
            
        return True
    
    def get_move_type(self):
        move_size = len(self.move)

        move_dict = {}
        for card in self.move:
            if card.get_type() not in move_dict:
                move_dict[card.get_type()] = 0

            move_dict[card.get_type()] += 1

        if move_size == 0:
            self.type = TYPE_0_PASS

        elif move_size == 1:
            self.type = TYPE_1_SINGLE

        elif move_size == 2:
            if self.move[0].get_type() == self.move[1].get_type():
                self.type = TYPE_2_PAIR
            else:
                self.type = TYPE_20_WRONG
                return

        elif move_size == 3:
            if len(move_dict) == 1:
                self.type = TYPE_3_TRIPLE
            elif self.is_continuous_seq():
                self.type = TYPE_5_SERIAL_SINGLE_3
            else:
                self.type = TYPE_20_WRONG
                return

        elif move_size == 4:
            if len(move_dict) == 1:
                self.type = TYPE_4_FOUROFKIND
            elif self.is_continuous_seq():
                self.type = TYPE_6_SERIAL_SINGLE_4
            else:
                self.type = TYPE_20_WRONG
                return

        elif move_size == 5:
            if self.is_continuous_seq():
                self.type = TYPE_7_SERIAL_SINGLE_5
            else:
                self.type = TYPE_20_WRONG
                return

        elif move_size == 6:
            if self.is_continuous_seq():
                self.type = TYPE_8_SERIAL_SINGLE_6
            elif len(move_dict) == 3:
                #NOTE: check for all pair
                for card_type in move_dict.keys():
                    if move_dict[card_type] != 2:
                        self.type = TYPE_20_WRONG
                        return
                    
                #NOTE: check for serial
                type_cards = list(move_dict.keys())
                for i in range(len(type_cards) - 1):
                    if type_cards[i + 1] - type_cards[i] != 1:
                        self.type = TYPE_20_WRONG
                        return
                self.type = TYPE_15_SERIAL_PAIR_3
            else:
                self.type = TYPE_20_WRONG
                return

        elif move_size == 7:
            if self.is_continuous_seq():
                self.type = TYPE_9_SERIAL_SINGLE_7
            else:
                self.type = TYPE_20_WRONG
                return

        elif move_size == 8:
            if self.is_continuous_seq():
                self.type = TYPE_10_SERIAL_SINGLE_8
            elif len(move_dict) == 4:
                #NOTE: check for all pair
                for card_type in move_dict.keys():
                    if move_dict[card_type] != 2:
                        self.type = TYPE_20_WRONG
                        return
                    
                #NOTE: check for serial
                type_cards = list(move_dict.keys())
                for i in range(len(type_cards) - 1):
                    if type_cards[i + 1] - type_cards[i] != 1:
                        self.type = TYPE_20_WRONG
                        return
                self.type = TYPE_16_SERIAL_PAIR_4
            else:
                self.type = TYPE_20_WRONG
                return
            
        elif move_size == 9:
            if self.is_continuous_seq():
                self.type = TYPE_11_SERIAL_SINGLE_9
            else:
                self.type = TYPE_20_WRONG
                return
            
        elif move_size == 10:
            if self.is_continuous_seq():
                self.type = TYPE_12_SERIAL_SINGLE_10
            elif len(move_dict) == 5:
                #NOTE: check for all pair
                for card_type in move_dict.keys():
                    if move_dict[card_type] != 2:
                        self.type = TYPE_20_WRONG
                        return
                    
                #NOTE: check for serial
                type_cards = list(move_dict.keys())
                for i in range(len(type_cards) - 1):
                    if type_cards[i + 1] - type_cards[i] != 1:
                        self.type = TYPE_20_WRONG
                        return
                self.type = TYPE_17_SERIAL_PAIR_5
            else:
                self.type = TYPE_20_WRONG
                return
            
        elif move_size == 11:
            if self.is_continuous_seq():
                self.type = TYPE_13_SERIAL_SINGLE_11
            else:
                self.type = TYPE_20_WRONG
                return
            
        elif move_size == 12:
            if self.is_continuous_seq():
                self.type = TYPE_14_SERIAL_SINGLE_12
            elif len(move_dict) == 6:
                #NOTE: check for all pair
                for card_type in move_dict.keys():
                    if move_dict[card_type] != 2:
                        self.type = TYPE_20_WRONG
                        return
                    
                self.type = TYPE_18_PAIR_6
            elif len(move_dict) == 4:
                #NOTE: check for all triplet
                for card_type in move_dict.keys():
                    if move_dict[card_type] != 3:
                        self.type = TYPE_20_WRONG
                        return
                    
                self.type = TYPE_19_TRIPLET_4
            else:
                self.type = TYPE_20_WRONG
                return
        else:
            self.type = TYPE_20_WRONG
            return

    def __getitem__(self, idx):
        return self.move[idx]

    def __len__(self):
        return len(self.move)
    
    def __eq__(self, __value) -> bool:
        if isinstance(__value, Move) and len(self.move) == len(__value):
            for i in range(len(__value)):
                if self.move[i] != __value[i]:
                    return False
            return True
        else:
            # don't attempt to compare against unrelated types
            return NotImplemented

    def __repr__(self):
        return f"{{{self.type}: {self.move} \n }}"