from pydantic import BaseModel, Field


class LeaveRoomReq(BaseModel):
    name: str = Field(default="", description="name bot")


class LeaveRoomRes(BaseModel):
    success: bool
