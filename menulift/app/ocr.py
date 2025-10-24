# app/ocr.py

import cv2
import easyocr
import os

# Initialize EasyOCR reader (English only for now)
reader = easyocr.Reader(["en"])


# 1. Preprocess image (resize, no grayscale)
def preprocess_image(image_path: str):
    img = cv2.imread(image_path)  # Read image in color (default BGR format)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  # Enlarge for better OCR
    return img


# 2. Run OCR on a single image
def run_ocr_on_image(image_path: str):
    # Step 1: Preprocess
    img = preprocess_image(image_path)

    # Step 2: Run OCR
    results = reader.readtext(img)

    # Step 3: Extract text only (ignore bounding boxes/confidence for now)
    extracted_text = [res[1] for res in results]

    return extracted_text


# 3. Run OCR on all images in a folder (menus/)
def run_ocr_on_folder(folder_path: str = "menus"):
    all_results = {}

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            file_path = os.path.join(folder_path, filename)
            text = run_ocr_on_image(file_path)
            all_results[filename] = text

    return all_results
