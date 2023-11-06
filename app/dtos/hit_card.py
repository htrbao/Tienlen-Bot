from pydantic import BaseModel, Field

class HitCardReq(BaseModel):
    bot_type: int = Field(default=0, description="bot type -1: random, 0: DMC, 1: SL")

    my_handcards: list[str] = Field(default=[], description="list card on bot hand")
    st_played_card: list[str] = Field(default=[], description="list card on first hand")
    nd_played_card: list[str] = Field(default=[], description="list card on secon hand")
    rd_played_card: list[str] = Field(default=[], description="list card on third hand")
    historical_action: list[list[str]] = Field(default=[[]], description="list of historical action of all user")

    legal_actions: list[list[str]] = Field(default=[[]], description="list of legal action based on my_handcards")


class HitCardRes(BaseModel):
    success: bool
    pred_action: list[str]
