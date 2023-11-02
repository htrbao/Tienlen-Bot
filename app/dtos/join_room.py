from pydantic import BaseModel, Field


class JoinRoomReq(BaseModel):
    bot_type: int = Field(default=0, description="bot type -1: random, 0: DMC, 1: SL")


class JoinRoomRes(BaseModel):
    success: bool
