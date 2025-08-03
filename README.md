# 🚇 PearlCard Fare Calculator

A full-stack web application for calculating metro fares in Pearly City using a prepaid NFC-enabled card system. Built with **Django (Python)** for the backend and **React (JavaScript)** for the frontend, styled with **Tailwind CSS**.

---

## 📌 Problem Statement

Transport officials in Pearly City are launching the **PearlCard**, a contactless prepaid card system for metro passengers. Fares are calculated based on fare zones:

| From-Zone | To-Zone | Fare (₹) |
|-----------|---------|----------|
| 1         | 1       | 40       |
| 1         | 2 / 2 → 1 | 55     |
| 1         | 3 / 3 → 1 | 65     |
| 2         | 2       | 35       |
| 2         | 3 / 3 → 2 | 45     |
| 3         | 3       | 30       |

---

## 💡 Features

- Submit up to 20 journeys in a day
- Fare is calculated based on zone pairs using backend logic
- Displays fare for each trip and total fare due
- Clean, responsive UI with Tailwind CSS
- Fully API-driven architecture

---

## ⚙️ Tech Stack

**Frontend:**
- React
- Axios (for API calls)
- Tailwind CSS

**Backend:**
- Django
- Django REST Framework
- CORS Headers

---

## 🚀 Getting Started

### 🔧 Backend Setup (Django)

```bash
# Clone the repo
cd pearlcard-project
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install django djangorestframework django-cors-headers

# Start project
cd backend
python manage.py migrate
python manage.py runserver
```

### 🌐 Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

The app will be available at: [http://localhost:3000](http://localhost:3000)

---

## 🧪 Sample API Request

`POST /api/calculate/`

```json
{
  "journeys": [
    { "from_zone": 1, "to_zone": 1 },
    { "from_zone": 1, "to_zone": 2 },
    { "from_zone": 3, "to_zone": 3 }
  ]
}
```

**Response:**
```json
{
  "journeys": [
    { "from_zone": 1, "to_zone": 1, "fare": 40 },
    { "from_zone": 1, "to_zone": 2, "fare": 55 },
    { "from_zone": 3, "to_zone": 3, "fare": 30 }
  ],
  "total_fare": 125
}
```

---

## 📁 Project Structure

```
pearlcard-project/
├── backend/         # Django backend
│   ├── fare/        # App with views and fare logic
│   └── ...
├── frontend/        # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── JourneyForm.jsx
│   │   │   └── FareTable.jsx
│   │   └── App.js
│   └── ...
```

---

## 📦 Future Enhancements

- User authentication (login/register)
- Fare history persistence with database
- Export trip summary to PDF
- Dynamic zone management via admin panel
- Deploy to Render (backend) + Vercel (frontend)

---

## 🛡 License

This project is licensed under the MIT License. See `LICENSE` file for details.

---

## 🙌 Acknowledgements

Built with ❤️ using Django, React, and Tailwind CSS.