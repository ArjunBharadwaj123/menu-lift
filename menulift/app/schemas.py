# app/schemas.py

from pydantic import BaseModel
from typing import List, Optional


# 1. Base schema for MenuItem (shared across create/read)
class MenuItemBase(BaseModel):
    name: str
    price: float


# 2. Schema for creating a MenuItem
class MenuItemCreate(MenuItemBase):
    section_id: int


# 3. Schema for reading a MenuItem (response)
class MenuItem(MenuItemBase):
    id: int
    section_id: int

    class Config:
        orm_mode = True


# 4. Base schema for MenuSection
class MenuSectionBase(BaseModel):
    name: str


# 5. Schema for creating a MenuSection
class MenuSectionCreate(MenuSectionBase):
    pass


# 6. Schema for reading a MenuSection (response)
class MenuSection(MenuSectionBase):
    id: int
    items: List[MenuItem] = []  # Include items when reading a section

    class Config:
        orm_mode = True
