from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.inventory import InventoryItem
from ..services.inventory_service import create_inventory_item, get_inventory_items, get_inventory_item, update_inventory_item, delete_inventory_item
from ..engine import get_db
from ..schemas.inventory import ItemCreate, Item
from typing import List

router = APIRouter()

@router.post("/inventory/additems", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_inventory_item(
        db=db,
        name=item.name,
        description=item.description,
        quantity=item.quantity,
        price=item.price
    )

@router.get("/inventory/", response_model=List[Item])
def read_items(db: Session = Depends(get_db)):
    return get_inventory_items(db=db)

@router.get("/inventory/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_inventory_item(db=db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/inventory/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    updated_item = update_inventory_item(
        db=db,
        item_id=item_id,
        name=item.name,
        description=item.description,
        quantity=item.quantity,
        price=item.price
    )
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/inventory/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = delete_inventory_item(db=db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
