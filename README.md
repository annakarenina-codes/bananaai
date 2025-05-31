## 🍌 BananaAI: AI-Powered Demand Forecasting System

**BananaAI** is a smart inventory management and demand forecasting system for small businesses. It integrates a Flask backend with a React.js frontend and uses XGBoost for future forecasting (in progress). The system includes basic authentication, secure protected routes, and a modular design for scalability.

---

### 📁 Project Structure

```
FINAL_PROJECT/
├── bananaai_backend/     # Flask backend
│   ├── app.py
│   ├── resources/
│   │   ├── product.py
│   │   ├── inventory.py
│   │   ├── sale.py
│   │   ├── forecast.py
│   │   ├── notification.py
│   ├── auth.py
│   ├── middleware.py
│   └── ...
└── bananaai_frontend/    # React frontend
    ├── src/
    │   ├── components/
    │   │   ├── AuthContext.jsx
    │   │   └── ProtectedRoute.jsx
    │   ├── pages/
    │   │   ├── LoginPage.jsx
    │   │   ├── RegisterPage.jsx
    │   │   └── UnauthorizedPage.jsx
    │   ├── utils/
    │   │   └── securityUtils.js
    │   ├── App.jsx
    │   └── main.jsx
    └── ...
```

---

### ✅ Features Implemented

#### 🔒 Authentication & Security

* `auth.py` – User registration and login (token-based)
* `middleware.py` – JWT authentication middleware
* Frontend AuthContext + ProtectedRoute implemented
* Users redirected based on auth status

#### 🔁 Backend API Endpoints

* CRUD operations for:

  * Products
  * Inventory
  * Sales
  * Notifications
* Basic `/forecast` route prepared for ML model integration

#### 💻 Frontend Components

* Secure Routing (`ProtectedRoute.jsx`)
* Context-based Auth Management (`AuthContext.jsx`)
* Login, Register, Unauthorized pages
* Basic UI wireframes and layout completed
* Connected mock API, to be integrated with backend

---

### 🚀 Setup Instructions

#### 📦 Backend Setup (`bananaai_backend`)

1. Create virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run backend:

   ```bash
   python app.py
   ```

#### 💻 Frontend Setup (`bananaai_frontend`)

1. Install dependencies:

   ```bash
   npm install
   ```
2. Start dev server:

   ```bash
   npm run dev
   ```

---

### 🌐 API Integration (Coming Soon)

* Connect `LoginPage` and `RegisterPage` to real `/login` and `/register` endpoints
* Save token to `localStorage`
* Decode token (optional) to show user info
* Pass token in request headers for protected endpoints




