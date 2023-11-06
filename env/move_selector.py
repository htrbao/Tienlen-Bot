# return all moves that can beat rivals, moves and rival_move should be same type
import collections
from copy import deepcopy

from app.pages.tienlen_bot.env.base.move import Move
from app.pages.tienlen_bot.env.utils.utils import *


def common_handle(moves: list[Move], rival_move: Move, move_type: int):
    new_moves = list()

    if not rival_move.type == move_type:
        raise ValueError(f"Rival move is not {move_type}")

    for move in moves:
        if move.type == rival_move.type and move.move[-1].id > rival_move.move[-1].id:
            new_moves.append(move)

    return new_moves

def filter_type_0_pass(moves: list[Move], rival_move: Move):
    return deepcopy(moves)

def filter_type_1_single(moves: list[Move], rival_move: Move):
    new_moves = common_handle(moves, rival_move, TYPE_1_SINGLE)
 
    if rival_move.move[-1].type == '2':
        for move in moves:
            if move.type in [TYPE_15_SERIAL_PAIR_3, TYPE_4_FOUROFKIND, TYPE_16_SERIAL_PAIR_4]:
                new_moves.append(move)

    return new_moves


def filter_type_2_pair(moves: list[Move], rival_move: Move):
    new_moves = common_handle(moves, rival_move, TYPE_2_PAIR)
 
    if rival_move.move[-1].type == '2':
        for move in moves:
                if move.type in [TYPE_4_FOUROFKIND, TYPE_16_SERIAL_PAIR_4]:
                    new_moves.append(move)

    return new_moves


def filter_type_3_triple(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_3_TRIPLE)


#NOTE: TỨ QUÝ
def filter_type_4_fourofkind(moves: list[Move], rival_move: Move):
    new_moves = common_handle(moves, rival_move, TYPE_4_FOUROFKIND)
 
    if rival_move.move[-1].type != '2':
        for move in moves:
            if move.type in [TYPE_16_SERIAL_PAIR_4]:
                new_moves.append(move)

    return new_moves


def filter_type_5_serial_single_3(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_5_SERIAL_SINGLE_3)


def filter_type_6_serial_single_4(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_6_SERIAL_SINGLE_4)


def filter_type_7_serial_single_5(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_7_SERIAL_SINGLE_5)


def filter_type_8_serial_single_6(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_8_SERIAL_SINGLE_6)


def filter_type_9_serial_single_7(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_9_SERIAL_SINGLE_7)


def filter_type_10_serial_single_8(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_10_SERIAL_SINGLE_8)


def filter_type_11_serial_single_9(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_11_SERIAL_SINGLE_9)


def filter_type_12_serial_single_10(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_12_SERIAL_SINGLE_10)


def filter_type_13_serial_single_11(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_13_SERIAL_SINGLE_11)

def filter_type_14_serial_single_12(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_14_SERIAL_SINGLE_12)


#NOTE: 3 ĐÔI THÔNG
def filter_type_15_serial_pair_3(moves: list[Move], rival_move: Move):
    new_moves = common_handle(moves, rival_move, TYPE_15_SERIAL_PAIR_3)

    for move in moves:
            if move.type in [TYPE_4_FOUROFKIND, TYPE_16_SERIAL_PAIR_4]:
                new_moves.append(move)

    return new_moves


#NOTE: 4 ĐÔI THÔNG
def filter_type_16_serial_pair_4(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_16_SERIAL_PAIR_4)


#NOTE: 5 ĐÔI THÔNG
def filter_type_17_serial_pair_5(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_17_SERIAL_PAIR_5)


#NOTE: 6 ĐÔI
def filter_type_18_pair_6(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_18_PAIR_6)


#NOTE: 4 XÁM CÔ
def filter_type_19_triplet_4(moves: list[Move], rival_move: Move):
    return common_handle(moves, rival_move, TYPE_19_TRIPLET_4)
