import axios from 'axios';

// Create axios instance with default config
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request interceptor to add auth token to requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Add response interceptor to handle common errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle 401 Unauthorized errors by redirecting to login
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    
    // Handle CSRF or other security errors
    if (error.response && error.response.status === 403) {
      console.error('Access forbidden:', error.response.data.message);
    }
    
    return Promise.reject(error);
  }
);

// Auth services
export const authService = {
  login: async (username, password) => {
    const response = await api.post('/auth/login', { username, password });
    if (response.data.token) {
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('user', JSON.stringify({
        id: response.data.user_id,
        username: response.data.username,
        role: response.data.role
      }));
    }
    return response.data;
  },
  
  register: async (userData) => {
    return await api.post('/auth/register', userData);
  },
  
  logout: () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  },
  
  getCurrentUser: () => {
    const userStr = localStorage.getItem('user');
    if (!userStr) return null;
    return JSON.parse(userStr);
  },
  
  isAuthenticated: () => {
    return !!localStorage.getItem('token');
  },
  
  hasRole: (roles) => {
    const user = authService.getCurrentUser();
    if (!user) return false;
    
    if (Array.isArray(roles)) {
      return roles.includes(user.role);
    }
    
    return user.role === roles;
  }
};

// Product services
export const productService = {
  getAll: async () => {
    const response = await api.get('/products');
    return response.data;
  },
  
  getById: async (id) => {
    const response = await api.get(`/products/${id}`);
    return response.data;
  },
  
  create: async (productData) => {
    const response = await api.post('/products', productData);
    return response.data;
  },
  
  update: async (id, productData) => {
    const response = await api.put(`/products/${id}`, productData);
    return response.data;
  },
  
  delete: async (id) => {
    const response = await api.delete(`/products/${id}`);
    return response.data;
  }
};

// Inventory services
export const inventoryService = {
  getSummary: async () => {
    const response = await api.get('/inventory');
    return response.data;
  }
};

// Sales services
export const salesService = {
  getAll: async () => {
    const response = await api.get('/sales');
    return response.data;
  },
  
  create: async (saleData) => {
    const response = await api.post('/sales', saleData);
    return response.data;
  }
};

// Forecast services
export const forecastService = {
  getForecast: async () => {
    const response = await api.get('/forecast');
    return response.data;
  }
};

// Notification services
export const notificationService = {
  getNotifications: async () => {
    const response = await api.get('/notifications');
    return response.data;
  },
  
  markAsRead: async (id) => {
    const response = await api.put(`/notifications/${id}/read`);
    return response.data;
  }
};

export default api;