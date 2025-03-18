from typing import Optional
from pydantic import BaseModel

class InventoryItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int
    price: float

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemSchema(InventoryItemBase):
    id: int

    class Config:
        orm_mode = True 