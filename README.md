
## 🍌 BananaAI: AI-Powered Demand Forecasting System

## 📌Overview

**BananaAI** is a Smart Inventory Demand Forecasting System designed to help small businesses with inventory management. The system uses machine learning (XGBoost model, to be integrated) to forecast the demand for products based on historical sales and inventory movements. It provides accurate demand predictions to help optimize stock levels and reduce wastage, ensuring the business runs efficiently.

## 📌Features

* **Backend**:
  * Implements a CRUD API using Flask for product, inventory movements, and forecasts.
  * PostgreSQL database to store products, inventory movements, and forecast data.
  * API endpoints to add, update, delete, and retrieve product information, inventory movements, and forecasts.
  * Forecast generation based on historical sales data.
  
* **Frontend**:
  * UI wireframe designed for an intuitive user experience.
  * Connected to the backend API to display product forecasts.
  * Deployed to Vercel for easy access and demonstration.

## 📌Backend Functionality:

### **API Endpoints**

1. **Products**:

   * `GET /products`: Retrieve all products.
   * `POST /products`: Add a new product.
   * `PUT /products/{id}`: Update an existing product.
   * `DELETE /products/{id}`: Delete a product.

2. **Inventory Movements**:

   * `GET /inventory_movements`: Retrieve all inventory movements.
   * `POST /inventory_movements`: Add a new inventory movement.
   * `DELETE /inventory_movements/{id}`: Delete an inventory movement.

3. **Forecasts**:

   * `GET /forecasts`: Retrieve all forecasts.
   * `POST /forecasts`: Generate and add new forecasts based on product sales and inventory data.
   * `PUT /forecasts/{id}`: Update an existing forecast.
   * `DELETE /forecasts/{id}`: Delete a forecast.

### **Implementation Details**

* **Flask Framework** for building the API.
* **PostgreSQL** as the database to store data.
* **XGBoost (future integration)** to generate demand forecasts based on inventory data.
* **SQLAlchemy** for database ORM and query building.

## 📌Frontend Progress

### **Completed Tasks**:

* **UI Wireframe Completed**: The initial wireframe design for the frontend has been finalized, outlining the basic structure for product and forecast views.
* **Mock API Connected**: The frontend is integrated with a mock API that simulates interaction with the backend to test functionality and display data.
* **Deployed to Vercel**: The frontend has been deployed and is accessible online, demonstrating the current UI along with the integration to the backend.

### **Next Steps for Frontend**:

1. **Integrate with Real API**: The mock API will be replaced with the real backend API.
2. **Develop Detailed Views**: More detailed views for product, inventory movements, and forecasts will be added, with user-friendly visualizations.
3. **Deploy to Production**: Finalize the design and deploy the application for use by actual small business clients.

## Next Steps for Backend

1. **Integrate XGBoost for Forecasting**: Replace the basic forecasting logic with an XGBoost model to predict demand based on historical sales data.
2. **Enhance Forecasting Logic**: Refine the forecasting algorithm, adding features like seasonality, promotions, and other factors affecting demand.
3. **Improve API Security**: Add user authentication and authorization to protect API endpoints.
4. **Unit Testing**: Write unit tests to ensure the API endpoints and business logic are functioning correctly.

## Project Structure

```
bananaai_backend/
├── app.py              # Main application file
├── models.py           # Database models
├── resources/          # Contains logic for CRUD operations
│   ├── product.py
│   ├── inventory.py
│   └── forecast.py
├── config.py           # Configuration for the app (e.g., database settings)
└── requirements.txt    # List of Python dependencies
```

