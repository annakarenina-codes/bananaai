# BananaAI - AI-Powered Demand Forecasting System

## Frontend Deployment URL:
- **Frontend Demo:** https://bananaaifrontend-git-main-anna-karenina-sanglays-projects.vercel.app

## Backend Progress:
- **Status**: The backend is under development. Current API routes are functional, but the database connection and optimization are in progress.
  - **Completed**: API routes for product data
  - **Completed**: Implemented all CRUD operations for all resources. 
  - **Completed**: Tested and confirmed all CRUD operations for Product, Inventory Movement, Sale, and Forecast.
    GET: Retrieved all data.
    POST: Added new data.
    GET by ID: Fetched specific data.
    PUT: Updated product data.
    DELETE: Removed data.

  - **In Progress**: Debugging 404 Not Found on /notifications Endpoint.

## Progress Overview:
- **Frontend**:
  - [x] UI wireframe completed
  - [x] Mock API connected
  - [x] Deployed to Vercel
- **Backend**:
  - [x] Flask API routes created
  - [x] PostgreSQL database connection 
  - [ ] Deployment to Heroku planned

  ## NEXT STEPS:
  1. **Fix /notifications 404 Error** → Check route registration and Blueprint setup.
  2. **Final CRUD Testing:** Once notifications are resolved, confirm all endpoints are fully tested.
  3. **Prepare for Frontend Integration:** Clean up API responses and optimize logic for easier frontend handling.
