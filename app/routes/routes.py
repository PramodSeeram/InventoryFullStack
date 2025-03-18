from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.inventory import InventoryItem
from ..models.schemas import InventoryItemCreate, InventoryItemSchema
from ..services.inventory_service import create_inventory_item, get_inventory_items, get_inventory_item, update_inventory_item, delete_inventory_item
from ..engine import get_db


router = APIRouter()


@router.post("/inventory/additems", response_model=InventoryItemSchema)
def create_item(item: InventoryItemCreate, db: Session = Depends(get_db)):
    return create_inventory_item(db=db, item=item)


@router.get("/inventory/", response_model=list[InventoryItemSchema])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_inventory_items(db=db, skip=skip, limit=limit)


@router.get("/inventory/{item_id}", response_model=InventoryItemSchema)
def read_item(item_id: int, db: Session = Depends(get_db)):
    return get_inventory_item(db=db, item_id=item_id)


@router.put("/inventory/{item_id}", response_model=InventoryItemSchema)
def update_item(item_id: int, item: InventoryItemCreate, db: Session = Depends(get_db)):
    return update_inventory_item(db=db, item_id=item_id, item=item)


@router.delete("/inventory/{item_id}", response_model=InventoryItemSchema)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return delete_inventory_item(db=db, item_id=item_id)
