from sqlalchemy.orm import Session
from ..models.inventory import InventoryItem as DBInventoryItem

def create_inventory_item(db: Session, name: str, description: str, quantity: int, price: float):
    db_item = DBInventoryItem(
        name=name,
        description=description,
        quantity=quantity,
        price=price
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_inventory_items(db: Session):
    return db.query(DBInventoryItem).all()

def get_inventory_item(db: Session, item_id: int):
    return db.query(DBInventoryItem).filter(DBInventoryItem.id == item_id).first()

def update_inventory_item(db: Session, item_id: int, name: str, description: str, quantity: int, price: float):
    db_item = db.query(DBInventoryItem).filter(DBInventoryItem.id == item_id).first()
    if db_item:
        db_item.name = name
        db_item.description = description
        db_item.quantity = quantity
        db_item.price = price
        db.commit()
        db.refresh(db_item)
        return db_item
    return None

def delete_inventory_item(db: Session, item_id: int):
    db_item = db.query(DBInventoryItem).filter(DBInventoryItem.id == item_id).first()
    if db_item:
        result = db_item
        db.delete(db_item)
        db.commit()
        return result
    return None 