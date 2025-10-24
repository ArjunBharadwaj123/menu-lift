# app/main.py

from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
import shutil

from . import models, schemas, crud
from .database import engine, Base, get_db
from .ocr import run_ocr_on_image
from .utils import parse_menu_text

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/upload/")
async def upload_menu(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = f"menus/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    raw_text = run_ocr_on_image(file_location)
    parsed_menu = parse_menu_text(raw_text)

    existing_sections = crud.get_sections(db)
    for section_name, items in parsed_menu.items():
        section = next((s for s in existing_sections if s.name == section_name), None)
        if section is None:
            section = crud.create_section(db, schemas.MenuSectionCreate(name=section_name))
            existing_sections.append(section)  # add to cache

        for item in items:
            crud.create_item(
                db,
                schemas.MenuItemCreate(
                    name=item["name"],
                    price=float(item["price"].replace("$", "")),
                    section_id=section.id,
                ),
            )

    return {"filename": file.filename, "parsed_menu": parsed_menu}