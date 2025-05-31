from flask import request, jsonify
from flask_restful import Resource
from ..models import User
from ..extensions import db
from ..auth import generate_token
from datetime import datetime

class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        
        # Data validation
        if not all(k in data for k in ('username', 'email', 'password')):
            return {'message': 'Missing required fields'}, 400
            
        # Check if user already exists
        if User.query.filter_by(username=data['username']).first():
            return {'message': 'Username already exists'}, 400
            
        if User.query.filter_by(email=data['email']).first():
            return {'message': 'Email already exists'}, 400
        
        # Create new user
        new_user = User(
            username=data['username'],
            email=data['email'],
            role=data.get('role', 'user')
        )
        new_user.set_password(data['password'])
        
        try:
            db.session.add(new_user)
            db.session.commit()
            return {'message': 'User created successfully'}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': f'Error creating user: {str(e)}'}, 500

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        
        # Data validation
        if not all(k in data for k in ('username', 'password')):
            return {'message': 'Missing username or password'}, 400
            
        # Authenticate user
        user = User.query.filter_by(username=data['username']).first()
        
        if user and user.check_password(data['password']):
            if not user.active:
                return {'message': 'Account is disabled'}, 403
                
            # Update last login time
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            # Generate token
            token = generate_token(user.id)
            
            return {
                'message': 'Login successful',
                'token': token,
                'user_id': user.id,
                'username': user.username,
                'role': user.role
            }, 200
        
        return {'message': 'Invalid credentials'}, 401