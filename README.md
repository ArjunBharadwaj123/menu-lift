# MenuLift 🍽️

MenuLift is an OCR-powered menu parsing system that extracts and categorizes restaurant menu items from image and PDF uploads.  
It uses **EasyOCR** and **OpenCV** for text extraction and layout analysis, then applies rule-based parsing to detect menu sections and items.  
The project includes a modular **FastAPI** backend and a lightweight **SQLite** database with **SQLAlchemy ORM** for structured storage of restaurants, menus, and items.

---

## 🚀 Features
- Upload restaurant menus in **image** or **PDF** format.  
- Perform **OCR** using EasyOCR and **layout analysis** with OpenCV.  
- Automatically detect **sections**, **item names**, **descriptions**, and **prices**.  
- Clean, rule-based post-processing using **regex** heuristics.  
- RESTful API endpoints for menu upload, parsing, and retrieval.  
- Modular and extensible **FastAPI** backend.  
- Lightweight **SQLite** database modeled with SQLAlchemy ORM.  
- Fully containerized with **Docker Compose** for reproducible deployment.

---

## 🧩 Tech Stack
**Backend:** FastAPI, Python, EasyOCR, OpenCV, SQLAlchemy  
**Database:** SQLite  
**Containerization:** Docker Compose  
**Testing:** Pytest  

---

## 📂 Project Structure
menulift/  
├── app/  
│   ├── main.py  
│   ├── models.py  
│   ├── routes/  
│   │   ├── upload.py  
│   │   └── parse.py  
│   ├── services/  
│   │   ├── ocr_service.py  
│   │   ├── parser_service.py  
│   │   └── utils.py  
│   ├── schemas/  
│   └── database.py  
├── tests/  
├── requirements.txt  
├── docker-compose.yml  
└── README.md  

---

## ⚙️ Setup & Run Locally

### 1. Clone the repo  
\`\`\`bash
git clone https://github.com/<your-username>/menulift.git
cd menulift
\`\`\`

### 2. Build and run the containers  
\`\`\`bash
docker-compose up --build
\`\`\`

The API will be available at \`http://localhost:8000\`  
Interactive Swagger docs: \`http://localhost:8000/docs\`

---

## 🧠 How It Works
1. The user uploads an image or PDF of a restaurant menu via the \`/upload\` endpoint.  
2. The file is passed through **EasyOCR** and **OpenCV** to extract text and identify layout positions.  
3. Parsed text is grouped into **sections** (e.g., Appetizers, Entrees, Desserts) using regex heuristics.  
4. Each detected item is stored in the database with name, description, price, and section references.  
5. Results can be queried through the API or used for analytics, search, or recommendation features.

---

## 📸 Demo
*(Optional: add screenshots or example JSON output from parsed menus)*

---

## 🧱 Example API Usage

### Upload a menu  
\`POST /upload\`  
**Body:** multipart/form-data (with \`file\` = menu image or PDF)

### Get all menu items  
\`GET /menus/{restaurant_id}/items\`

Example Response:  
\`\`\`json
{
  "restaurant": "Sample Bistro",
  "menu_items": [
    { "section": "Appetizers", "name": "Bruschetta", "price": 8.5 },
    { "section": "Entrees", "name": "Grilled Salmon", "price": 18.0 }
  ]
}
\`\`\`

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

## 🪪 License
MIT License – see \`LICENSE\` for details.
