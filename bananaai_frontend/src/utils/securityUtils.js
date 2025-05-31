/**
 * Security utility functions for client-side security
 */

/**
 * Sanitize string input to prevent XSS attacks
 * @param {string} input - The string to sanitize
 * @returns {string} Sanitized string
 */
export const sanitizeInput = (input) => {
  if (!input) return '';
  
  const el = document.createElement('div');
  el.innerText = input;
  return el.innerHTML;
};

/**
 * Validate email format
 * @param {string} email - Email to validate
 * @returns {boolean} Whether email is valid
 */
export const isValidEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

/**
 * Check if password meets security requirements
 * @param {string} password - Password to validate
 * @returns {object} Validation result with error message
 */
export const validatePassword = (password) => {
  if (!password) {
    return { valid: false, message: 'Password is required' };
  }
  
  if (password.length < 8) {
    return { valid: false, message: 'Password must be at least 8 characters' };
  }
  
  // Check for at least one uppercase letter
  if (!/[A-Z]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one uppercase letter' };
  }
  
  // Check for at least one lowercase letter
  if (!/[a-z]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one lowercase letter' };
  }
  
  // Check for at least one number
  if (!/[0-9]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one number' };
  }
  
  // Check for at least one special character
  if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one special character' };
  }
  
  return { valid: true, message: 'Password is valid' };
};

/**
 * Encode URI component safely
 * @param {string} value - Value to encode
 * @returns {string} Encoded value
 */
export const safeEncodeURIComponent = (value) => {
  if (!value) return '';
  return encodeURIComponent(value.toString());
};

/**
 * Generate a Content Security Policy nonce
 * @returns {string} CSP nonce value
 */
export const generateCSPNonce = () => {
  const array = new Uint8Array(16);
  window.crypto.getRandomValues(array);
  return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
};

/**
 * Check if token is expired
 * @param {string} token - JWT token
 * @returns {boolean} Whether token is expired
 */
export const isTokenExpired = (token) => {
  if (!token) return true;
  
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split('')
        .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    );

    const { exp } = JSON.parse(jsonPayload);
    return exp * 1000 < Date.now();
  } catch (error) {
    console.error('Error checking token expiration:', error);
    return true;
  }
};

/**
 * Convert potentially dangerous HTML to safe text
 * @param {string} html - HTML string to make safe
 * @returns {string} Safe text
 */
export const htmlToSafeText = (html) => {
  if (!html) return '';
  
  const temp = document.createElement('div');
  temp.innerHTML = html;
  return temp.textContent || temp.innerText || '';
};

/**
 * Check if a given input is a valid number within range
 * @param {any} value - Value to check
 * @param {number} min - Minimum allowed value
 * @param {number} max - Maximum allowed value
 * @returns {boolean} Whether input is valid
 */
export const isValidNumberInput = (value, min, max) => {
  const num = Number(value);
  if (isNaN(num)) return false;
  if (min !== undefined && num < min) return false;
  if (max !== undefined && num > max) return false;
  return true;
};

/**
 * Get CSRF token from meta tag
 * @returns {string|null} CSRF token if found
 */
export const getCSRFToken = () => {
  const metaTag = document.querySelector('meta[name="csrf-token"]');
  return metaTag ? metaTag.getAttribute('content') : null;
};