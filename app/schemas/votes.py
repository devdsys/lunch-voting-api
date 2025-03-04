from pydantic import BaseModel
from datetime import datetime

class VoteBase(BaseModel):
    menu_id: int
    stars: int

class VoteCreate(VoteBase):
    pass

class Vote(VoteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True