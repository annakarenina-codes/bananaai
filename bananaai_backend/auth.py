from flask import request, jsonify, current_app
from functools import wraps
import jwt
from datetime import datetime, timedelta
from .models import User
from .extensions import db

def generate_token(user_id):
    """Generate JWT token for authenticated users"""
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(
        payload,
        current_app.config.get('SECRET_KEY'),
        algorithm='HS256'
    )

def token_required(f):
    """Decorator for routes that require authentication"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # Get token from Authorization header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
        
        if not token:
            return jsonify({'message': 'Authentication token is missing'}), 401
        
        try:
            # Decode the token
            data = jwt.decode(
                token, 
                current_app.config.get('SECRET_KEY'),
                algorithms=['HS256']
            )
            current_user = User.query.filter_by(id=data['sub']).first()
            
            if not current_user:
                return jsonify({'message': 'Invalid authentication token'}), 401
                
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
            
        return f(current_user, *args, **kwargs)
    
    return decorated

def role_required(roles):
    """Decorator for routes that require specific roles"""
    def decorator(f):
        @wraps(f)
        def decorated_function(current_user, *args, **kwargs):
            if current_user.role not in roles:
                return jsonify({'message': 'Insufficient permissions'}), 403
            return f(current_user, *args, **kwargs)
        return decorated_function
    return decorator