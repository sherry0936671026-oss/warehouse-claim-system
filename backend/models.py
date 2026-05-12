from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime


class Warehouse(SQLModel, table=True):
    wh_id: str = Field(primary_key=True)
    wh_name: str
    region: str


class Item(SQLModel, table=True):
    item_id: str = Field(primary_key=True)
    item_name: str
    category: str


class ClaimEvent(SQLModel, table=True):
    event_id: str = Field(primary_key=True)
    from_wh: str = Field(foreign_key="warehouse.wh_id")
    to_wh: str = Field(foreign_key="warehouse.wh_id")
    item_id: str = Field(foreign_key="item.item_id")
    prb_code: str
    qty_claimed: int
    status: str = "待確認"
    note: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)


class EventLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: str = Field(foreign_key="claimevent.event_id")
    action: str
    actor_wh: str
    note: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)