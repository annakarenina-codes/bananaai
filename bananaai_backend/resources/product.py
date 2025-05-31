from flask import request, jsonify
from flask_restful import Resource
from ..models import Product
from ..extensions import db
from ..auth import token_required, role_required

class ProductResource(Resource):
    @token_required
    def get(self, current_user, product_id):
        """Get a specific product by ID"""
        product = Product.query.get_or_404(product_id)
        return {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'quantity': product.quantity,
            'created_at': product.created_at.isoformat(),
            'updated_at': product.updated_at.isoformat() if product.updated_at else None
        }
    
    @token_required
    @role_required(['admin', 'manager'])
    def put(self, current_user, product_id):
        """Update a product"""
        product = Product.query.get_or_404(product_id)
        data = request.get_json()
        
        if 'name' in data:
            product.name = data['name']
        if 'description' in data:
            product.description = data['description']
        if 'price' in data:
            product.price = data['price']
        if 'quantity' in data:
            product.quantity = data['quantity']
            
        try:
            db.session.commit()
            return {'message': 'Product updated successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': f'Error updating product: {str(e)}'}, 500
    
    @token_required
    @role_required(['admin'])
    def delete(self, current_user, product_id):
        """Delete a product"""
        product = Product.query.get_or_404(product_id)
        
        try:
            db.session.delete(product)
            db.session.commit()
            return {'message': 'Product deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': f'Error deleting product: {str(e)}'}, 500

class ProductListResource(Resource):
    @token_required
    def get(self, current_user):
        """Get all products"""
        products = Product.query.all()
        return [
            {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'quantity': product.quantity,
                'created_at': product.created_at.isoformat(),
                'updated_at': product.updated_at.isoformat() if product.updated_at else None
            } for product in products
        ]
    
    @token_required
    @role_required(['admin', 'manager'])
    def post(self, current_user):
        """Create a new product"""
        data = request.get_json()
        
        # Data validation
        if not all(k in data for k in ('name', 'price')):
            return {'message': 'Missing required fields'}, 400
            
        new_product = Product(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
            quantity=data.get('quantity', 0)
        )
        
        try:
            db.session.add(new_product)
            db.session.commit()
            return {
                'message': 'Product created successfully',
                'product_id': new_product.id
            }, 201
        except Exception as e:
            db.session.rollback()
            return {'message': f'Error creating product: {str(e)}'}, 500