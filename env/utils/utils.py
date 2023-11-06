from typing import List, Iterable

import numpy as np

from env.base import Card

import itertools

# global parameters
MIN_SINGLE_CARDS = 5
MIN_PAIRS = 3
MIN_TRIPLES = 2

# action types
TYPE_0_PASS = 0
TYPE_1_SINGLE = 1
TYPE_2_PAIR = 2
TYPE_3_TRIPLE = 3
TYPE_4_FOUROFKIND = 4

TYPE_5_SERIAL_SINGLE_3 = 5
TYPE_6_SERIAL_SINGLE_4 = 6
TYPE_7_SERIAL_SINGLE_5 = 7
TYPE_8_SERIAL_SINGLE_6 = 8
TYPE_9_SERIAL_SINGLE_7 = 9
TYPE_10_SERIAL_SINGLE_8 = 10
TYPE_11_SERIAL_SINGLE_9 = 11
TYPE_12_SERIAL_SINGLE_10 = 12
TYPE_13_SERIAL_SINGLE_11 = 13 
TYPE_14_SERIAL_SINGLE_12 = 14 #SẢNH RỒNG ĂN TRẮNG

TYPE_15_SERIAL_PAIR_3 = 15
TYPE_16_SERIAL_PAIR_4 = 16
TYPE_17_SERIAL_PAIR_5 = 17 #5 ĐÔI THÔNG ĂN TRẮNG

TYPE_18_PAIR_6 = 18 #6 ĐÔI ĂN TRẮNG
TYPE_19_TRIPLET_4 = 19 #4 XÁM CÔ ĂN TRẮNG

TYPE_20_WRONG = 20

# return all possible results of selecting num cards from cards list
def select(cards, num):
    return [list(i) for i in itertools.combinations(cards, num)]

def card_from_card_id(card_id: int) -> Card:
    return Card(card_id)

# deck is always in order from AS, 2S, ..., AH, 2H, ..., AD, 2D, ..., AC, 2C, ... QC, KC
# _deck = [card_from_card_id(card_id) for card_id in range(52)]  # want this to be read-only
