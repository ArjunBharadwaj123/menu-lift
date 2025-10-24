# app/models.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# 1. MenuSection model - represents sections like Breakfast, Lunch, etc.
class MenuSection(Base):
    __tablename__ = "menu_sections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)

    # Relationship: a section has many items
    items = relationship("MenuItem", back_populates="section")


# 2. MenuItem model - represents individual food/drink items
class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

    section_id = Column(Integer, ForeignKey("menu_sections.id"))

    # Relationship: an item belongs to one section
    section = relationship("MenuSection", back_populates="items")
