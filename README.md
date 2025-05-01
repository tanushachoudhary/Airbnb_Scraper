# 🏡 Airbnb Clone – Fullstack Project

This is a full-stack Airbnb-style application built using:

- **Backend:** Django REST Framework + MySQL
- **Frontend:** ReactJS (or Next.js) with Tailwind CSS
- **Scraper:** Scrapy (Python) for collecting Airbnb listings

---

## 📁 Project Structure

```
airbnb-clone/
├── backend/               # Django + DRF backend
│   ├── airbnb_api/        # Django project
│   └── listings/          # App for managing listings
├── frontend/              # ReactJS or Next.js + Tailwind CSS frontend
├── scraper/               # Scrapy spider for Airbnb data
│   └── airbnb/            # Scrapy project
```

---

## ⚙️ Requirements

### 🔧 Backend

- Python 3.9+
- Django 4.x
- Django REST Framework
- MySQL Server
- MySQL client (`mysqlclient` or `pymysql`)

### 🎨 Frontend

- Node.js + npm
- React or Next.js
- Tailwind CSS

### 🕷 Scraper

- Scrapy 2.12+
- Requests

---

## 🛠 Setup Instructions

### 🔌 MySQL Setup

1. Open **MySQL Workbench** or terminal and run:

```sql
CREATE DATABASE airbnb_db;
```

2. Update `backend/airbnb_api/settings.py` with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'airbnb_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 🚀 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # on Windows
pip install -r ../requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

APIs:

- `GET /api/listings/` – Retrieve all listings
- `POST /api/add_listing/` – Add a new listing

---

### 🌐 Frontend Setup

```bash
cd frontend
npm install
npm run dev  # or npm run start for Next.js
```

Frontend shows:
- Search Results Page
- Individual Listing Page

Filters: location, check-in/out, guests, price, ratings.

---

### 🕷 Scraper Setup

```bash
cd scraper
python -m venv venv
venv\Scripts\activate  # on Windows
pip install scrapy requests
cd airbnb
scrapy crawl airbnb
```

> 📌 Sends scraped mock data to `http://localhost:8000/api/add_listing`.

---

## 🔗 Sample API POST Call (from Scraper)

```python
import requests

data = {
  "title": "Cozy Apartment in NYC",
  "location": "New York, USA",
  "price_per_night": 120,
  "ratings": 4.8,
  "reviews": 150,
  "amenities": ["WiFi", "Kitchen", "Air Conditioning"],
  "host": {
      "name": "John",
      "superhost": True,
      "profile_url": "https://airbnb.com/users/123"
  },
  "property_type": "Apartment"
  # other fields...
}

response = requests.post("http://localhost:8000/api/add_listing/", json=data)
print(response.status_code)
```

---

## 🧾 License

MIT License
