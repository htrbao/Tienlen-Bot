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


@app.options("/tienlen_bots/hit-cards")
def bot_hit_cards(req: HitCardReq) -> HitCardRes:
    pred_action = pool.predict_action(req)

    
    return HitCardRes(success=True, pred_action=pred_action)