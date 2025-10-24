# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas


# 1. Create a new menu section
def create_section(db: Session, section: schemas.MenuSectionCreate):
    db_section = models.MenuSection(name=section.name)
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section


# 2. Get all menu sections
def get_sections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MenuSection).offset(skip).limit(limit).all()


# 3. Create a new menu item
def create_item(db: Session, item: schemas.MenuItemCreate):
    # Check if item already exists in this section
    existing_item = (
        db.query(models.MenuItem)
        .filter(
            models.MenuItem.name == item.name,
            models.MenuItem.section_id == item.section_id
        )
        .first()
    )
    if existing_item:
        return existing_item
    
    # Otherwise create new
    db_item = models.MenuItem(
        name=item.name, price=item.price, section_id=item.section_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# 4. Get all menu items in a section
def get_items_by_section(db: Session, section_id: int):
    return (
        db.query(models.MenuItem)
        .filter(models.MenuItem.section_id == section_id)
        .all()
    )
