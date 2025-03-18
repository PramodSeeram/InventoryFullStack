from sqlalchemy.orm import Session
from ..models.inventory import InventoryItem as DBInventoryItem
from ..models.schemas import InventoryItemCreate

def create_inventory_item(db: Session, item: InventoryItemCreate):
    db_item = DBInventoryItem(
        name=item.name,
        description=item.description,
        quantity=item.quantity,
        price=item.price
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_inventory_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DBInventoryItem).offset(skip).limit(limit).all()

def get_inventory_item(db: Session, item_id: int):
    return db.query(DBInventoryItem).filter(DBInventoryItem.id == item_id).first()

def update_inventory_item(db: Session, item_id: int, item: InventoryItemCreate):
    db_item = db.query(DBInventoryItem).filter(DBInventoryItem.id == item_id).first()
    if db_item:
        update_data = item.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_inventory_item(db: Session, item_id: int):
    db_item = db.query(DBInventoryItem).filter(DBInventoryItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item 