import collections
import itertools
from copy import deepcopy
import numpy as np

from app.pages.tienlen_bot.env.base import Card, Move
from app.pages.tienlen_bot.env.utils.utils import *

class MovesGener(object):
    """
    This is for generating the possible combinations
    """
    def __init__(self, cards_list: list[Card]):
        self.cards: list[Card] = []
        for card in cards_list:
            self.cards.append(card)
        self.cards.sort(key=lambda x: x.id)

        self.cards_dict: dict[int, list[Card]] = {}
        for card in self.cards:
            if card.get_type() not in self.cards_dict:
                self.cards_dict[card.get_type()] = []
            
            self.cards_dict[card.get_type()].append(card)


    def gen_type_serial_single(self, length: int, type_card: int, serial_single_move: list[Card], moves: list[Move]):
        if type_card not in self.cards_dict:
            return 
        for card in self.cards_dict[type_card]:
            serial_single_move.append(card)
            if len(serial_single_move) == length:
                moves.append(Move(serial_single_move))
            else:
                self.gen_type_serial_single(length, type_card + 1, serial_single_move, moves)
            serial_single_move.pop()


    def gen_type_serial_pair(self, length: int, type_card: int, serial_pair_move: list[Card], moves: list[Move]):
        if type_card not in self.cards_dict or len(self.cards_dict[type_card]) < 2:
            return

        for i in itertools.combinations(self.cards_dict[type_card], 2):
            serial_pair_move.extend(list(i))
            if len(serial_pair_move) == length:
                moves.append(Move(serial_pair_move))
            else:
                self.gen_type_serial_pair(length, type_card + 1, serial_pair_move, moves)
            serial_pair_move.pop()
            serial_pair_move.pop()


    def gen_type_triple(self, length: int, type_card: int, triple_move: list[Card], moves: list[Move]):
        if type_card not in self.cards_dict or len(self.cards_dict[type_card]) < 3:
            return

        for i in itertools.combinations(self.cards_dict[type_card], 3):
            triple_move.extend(list(i))
            if len(triple_move) == length:
                moves.append(Move(triple_move))
            else:
                self.gen_type_serial_pair(length, type_card + 1, triple_move, moves)
            triple_move.pop()
            triple_move.pop()
            triple_move.pop()

    # **************************************************************************************************** #

    def _gen_type_1_single(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(1, i, [], moves)

        return moves

    def _gen_type_2_pair(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_pair(2, i, [], moves)

        return moves

    def _gen_type_3_triple(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_triple(3, i, [], moves)

        return moves

    def _gen_type_4_four_of_kind(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            if len(self.cards_dict[i]) == 4:
                moves.append(Move(self.cards_dict[i]))

        return moves

    def _gen_type_5_serial_single_3(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(3, i, [], moves)

        return moves

    def _gen_type_6_serial_single_4(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(4, i, [], moves)

        return moves

    def _gen_type_7_serial_single_5(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(5, i, [], moves)

        return moves

    def _gen_type_8_serial_single_6(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(6, i, [], moves)

        return moves

    def _gen_type_9_serial_single_7(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(7, i, [], moves)

        return moves

    def _gen_type_10_serial_single_8(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(8, i, [], moves)

        return moves

    def _gen_type_11_serial_single_9(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(9, i, [], moves)

        return moves

    def _gen_type_12_serial_single_10(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(10, i, [], moves)

        return moves

    def _gen_type_13_serial_single_11(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(11, i, [], moves)

        return moves
    
    def _gen_type_14_serial_single_12(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_single(12, i, [], moves)

        return moves

    def _gen_type_15_serial_pair_3(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_pair(6, i, [], moves)

        return moves

    def _gen_type_16_serial_pair_4(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_pair(8, i, [], moves)

        return moves

    def _gen_type_17_serial_pair_5(self):
        moves: list[Move] = []
        for i in self.cards_dict.keys():
            self.gen_type_serial_pair(10, i, [], moves)

        return moves

    def _gen_type_18_pair_6(self):
        moves_lst: list[list[Card]] = []

        is_have_triplet = False
        # * Khi có 6 đôi thì tối đa có 1 triplet
        count_pair = 0
        for k in self.cards_dict.keys():
            if len(self.cards_dict[k]) < 2:
                return []
            if len(self.cards_dict[k]) == 3:
                is_have_triplet = True
            count_pair += 1

        if count_pair != 6:
            return []
        
        moves_lst = [[], [], []] if is_have_triplet else []

        for k in self.cards_dict.keys():
            if len(self.cards_dict[k]) == 2:
                for i in range(len(moves_lst)):
                    moves_lst[i].extend(self.cards_dict[k])
            elif len(self.cards_dict[k]) == 3:
                lst = [list(i) for i in itertools.combinations(self.cards_dict[k], 2)]
                for i in range(len(lst)):
                    moves_lst[i].extend(lst[i])

        return [Move(x) for x in moves_lst]

    def _gen_type_19_triplet_4(self):
        moves_lst: list[list[Card]] = []

        is_have_four_of_kind = False
        # * Khi có 4 xám thì tối đa có 1 Tứ Quý
        count_triple = 0
        for k in self.cards_dict.keys():
            if len(self.cards_dict[k]) < 3:
                return []
            if len(self.cards_dict[k]) == 4:
                is_have_four_of_kind = True
            count_triple += 1

        if count_triple != 4:
            return []
        
        moves_lst = [[], [], [], []] if is_have_four_of_kind else []

        for k in self.cards_dict.keys():
            if len(self.cards_dict[k]) == 3:
                for i in range(len(moves_lst)):
                    moves_lst[i].extend(self.cards_dict[k])
            elif len(self.cards_dict[k]) == 4:
                lst = [list(i) for i in itertools.combinations(self.cards_dict[k], 3)]
                for i in range(len(lst)):
                    moves_lst[i].extend(lst[i])

        return [Move(x) for x in moves_lst]

    def _gen_all_type(self):
        moves: list[Move] = []

        moves.extend(self._gen_type_1_single())
        moves.extend(self._gen_type_2_pair())
        moves.extend(self._gen_type_3_triple())
        moves.extend(self._gen_type_4_four_of_kind())

        moves.extend(self._gen_type_5_serial_single_3())
        moves.extend(self._gen_type_6_serial_single_4())
        moves.extend(self._gen_type_7_serial_single_5())
        moves.extend(self._gen_type_8_serial_single_6())
        moves.extend(self._gen_type_9_serial_single_7())
        moves.extend(self._gen_type_10_serial_single_8())
        moves.extend(self._gen_type_11_serial_single_9())
        moves.extend(self._gen_type_12_serial_single_10())
        moves.extend(self._gen_type_13_serial_single_11())
        moves.extend(self._gen_type_14_serial_single_12())

        moves.extend(self._gen_type_15_serial_pair_3())
        moves.extend(self._gen_type_16_serial_pair_4())
        moves.extend(self._gen_type_17_serial_pair_5())

        moves.extend(self._gen_type_18_pair_6())

        moves.extend(self._gen_type_19_triplet_4())

        return moves