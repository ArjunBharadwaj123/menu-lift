# app/utils.py

import re
from typing import List, Dict


# --- Price Helpers ---
def clean_price(text: str) -> str:
    # Case 1: Starts with S or 5 (OCR errors for $) → allow integer or decimal
    if re.match(r"^[S5]\d+(\.\d{1,2})?$", text):
        text = "$" + text[1:]
    # Case 2: Just digits (int or decimal)
    elif re.match(r"^\d+(\.\d{1,2})?$", text):
        text = "$" + text
    return text

def is_price(text: str) -> bool:
    print("Text: " + text)
    print(bool(re.match(r"^[S5]\d+(\.\d{1,2})?$", text)))
    print(bool(re.match(r"^\d+(\.\d{1,2})?$", text)))
    return bool(
        re.match(r"^[S5]\d+(\.\d{1,2})?$", text) or re.match(r"^\d+(\.\d{1,2})?$", text)
    )


# --- Section + Item Parsing ---
from typing import List, Dict

def parse_menu_text(text_lines: List[str]) -> Dict[str, List[Dict[str, str]]]:
    menu = {}
    current_section = None
    used_items = set()   # ✅ Track items already assigned to a section

    for i, line in enumerate(text_lines):
        line = line.strip()

        print("LINE: " + line)

        # Skip empty/junk lines
        if not line or line.lower() in ["menu", "restaurant", "www.companyname.com"]:
            continue


        # --- Detect Section Header ---
        if (
            not is_price(line)
            # and len(line.split()) <= 3
            # and (line.isupper() or line.istitle())
            and (i + 2 < len(text_lines) and is_price(text_lines[i + 2]))
        ):
            print("This is a section header: " + line)
            if line.lower() not in used_items:   # ✅ skip if already used as item
                current_section = line
                if current_section not in menu:
                    menu[current_section] = []
            continue

        # print("Current Section: " + current_section)
        if is_price(line) and current_section:
            print("This is not a section header: " + text_lines[i-1] + ": " + line)
            cleaned_price = clean_price(line)
            item_name = text_lines[i - 1].strip()

            print("Item: Price ---> " + item_name + ": " + cleaned_price)

            if not is_price(item_name):
                menu[current_section].append(
                    {"name": item_name, "price": cleaned_price}
                )
                used_items.add(item_name.lower())   # ✅ mark lowercase to prevent dupes
            continue  # ✅ don’t let this same line be mistaken as a section

    return menu

