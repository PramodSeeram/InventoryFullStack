from sqlalchemy.orm import Session
from ..models.inventory import InventoryItem

# Create inventory item
def create_inventory_item(db: Session, item: InventoryItem):
    db_item = InventoryItem(name=item.name, description=item.description, quantity=item.quantity, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Get all inventory items
def get_inventory_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InventoryItem).offset(skip).limit(limit).all()

# Get a single inventory item by ID
def get_inventory_item(db: Session, item_id: int):
    return db.query(InventoryItem).filter(InventoryItem.id == item_id).first()

# Update inventory item by ID
def update_inventory_item(db: Session, item_id: int, item: InventoryItem):
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.description = item.description
        db_item.quantity = item.quantity
        db_item.price = item.price
        db.commit()
        db.refresh(db_item)
    return db_item

# Delete inventory item by ID
def delete_inventory_item(db: Session, item_id: int):
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
