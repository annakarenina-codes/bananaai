# config.py

import os
from datetime import timedelta

class Config:
    #Basic Class Config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    TESTING = False

    #Database Config
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:micah7:8@localhost/bananaai_new'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    #Security Headers
    SECURITY_HEADERS = {
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'SAMEORIGIN',
        'X-XSS-Protection': '1; mode=block',
        'Content-Security-Policy': "default-src 'self'; script-src 'self'; connect-src 'self'; img-src 'self'; style-src 'self';",
        'Strict-Transport-Security': 'max-age=31536000; includeSubDomains'
    }
    #CORS settings
    ALLOWED_ORIGINS = os.environ.get('ALLOWED_ORIGINS', 'http://localhost:5000').split(',')

    #Session settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)

    #Password hashing - higher number = more secure but slower
    BCRYPT_LOG_ROUNDS = 12

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False  # For development without HTTPS
    
class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    # Use in-memory database for testing
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SESSION_COOKIE_SECURE = False
    
class ProductionConfig(Config):
    # For production, SECRET_KEY must be set from environment
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for production environment")
    
    # Force HTTPS in production
    SESSION_COOKIE_SECURE = True
    
    # Increase bcrypt rounds for production
    BCRYPT_LOG_ROUNDS = 14
    
    # Database should be set via environment variable
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("No DATABASE_URI set for production environment")

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
