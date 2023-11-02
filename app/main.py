from typing import Union
from fastapi import FastAPI, Depends

from .bot_pool import BotPool
from .config import get_settings

from .dtos import *

app = FastAPI()
pool = BotPool(get_settings().accounts)

@app.get("/tienlen_bots")
def bot() -> list[dict]:
    res = []
    for account in get_settings().accounts:
        print(account)
        res.append(account)
    return res


@app.get("/tienlen_bots/actives")
def bot_infos() -> list[BotInfo]:
    infos = []
    for bot in pool.bots:
        infos.append(BotInfo.create(bot))

    return infos


@app.post("/tienlen_bots/join-table")
def bot_join_table(req: JoinRoomReq) -> JoinRoomRes:
    bot = pool.create_bot(req.bot_type)

    print(bot)

    if bot is None:
        return JoinRoomRes(success=False)
    
    return JoinRoomRes(success=True)


@app.post("/tienlen_bots/leave-table")
def bot_leave_table(req: LeaveRoomReq) -> LeaveRoomRes:
    return LeaveRoomRes(success=True)
