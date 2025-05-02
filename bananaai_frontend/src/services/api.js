// src/services/api.js
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Products API
export const productAPI = {
  getAll: () => api.get('/api/products'),
  getById: (id) => api.get(`/api/products/${id}`),
  create: (data) => api.post('/api/products', data),
  update: (id, data) => api.put(`/api/products/${id}`, data),
  delete: (id) => api.delete(`/api/products/${id}`),
  getForecasts: (id) => api.get(`/api/products/${id}/forecasts`),
};

// Sales API
export const saleAPI = {
  getAll: () => api.get('/api/sales'),
  getById: (id) => api.get(`/api/sales/${id}`),
  create: (data) => api.post('/api/sales', data),
};

// Inventory API
export const inventoryAPI = {
  getAll: () => api.get('/api/inventory'),
  getById: (id) => api.get(`/api/inventory/${id}`),
  create: (data) => api.post('/api/inventory', data),
  delete: (id) => api.delete(`/api/inventory/${id}`),
};

// Forecast API
export const forecastAPI = {
  getAll: () => api.get('/api/forecasts'),
  getById: (id) => api.get(`/api/forecasts/${id}`),
  generate: (data) => api.post('/api/forecasts', data),
};

// Notification API
export const notificationAPI = {
  getAll: (status) => api.get('/api/notifications', { params: { status } }),
  getById: (id) => api.get(`/api/notifications/${id}`),
  create: (data) => api.post('/api/notifications', data),
  update: (id, data) => api.put(`/api/notifications/${id}`, data),
  delete: (id) => api.delete(`/api/notifications/${id}`),
  generateSystem: () => api.post('/api/system/notifications'),
};

export default {
  product: productAPI,
  sale: saleAPI,
  inventory: inventoryAPI,
  forecast: forecastAPI,
  notification: notificationAPI,
};