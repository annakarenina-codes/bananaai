from flask import request
from flask_restful import Resource
from bananaai_backend.extensions import db
from bananaai_backend.models import Product
from datetime import datetime

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return [
            {
                'id': product.id,
                'name': product.name,
                'category': product.category,
                'product_type': product.product_type,
                'expiry_date': product.expiry_date.isoformat() if product.expiry_date else None,
                'price': product.price,
                'total_stock': product.total_stock,
                'stock_sold': product.stock_sold,
                'stock_restocked': product.stock_restocked,
                'available_stock': product.available_stock,
                'location': product.location
            } for product in products
        ]
    
    def post(self):
        data = request.get_json()
        
        # Parse expiry date if provided
        expiry_date = None
        if data.get('expiry_date'):
            try:
                expiry_date = datetime.fromisoformat(data['expiry_date'])
            except ValueError:
                return {'message': 'Invalid expiry date format'}, 400
        
        new_product = Product(
            name=data['name'],
            category=data.get('category'),
            product_type=data.get('product_type', 'non-perishable'),
            expiry_date=expiry_date,
            price=data['price'],
            total_stock=data.get('total_stock', 0),
            stock_sold=data.get('stock_sold', 0),
            stock_restocked=data.get('stock_restocked', 0),
            available_stock=data.get('available_stock', 0),
            location=data.get('location')
        )
        
        db.session.add(new_product)
        db.session.commit()
        
        return {
            'message': 'Product created successfully',
            'id': new_product.id
        }, 201

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return {
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'product_type': product.product_type,
            'expiry_date': product.expiry_date.isoformat() if product.expiry_date else None,
            'price': product.price,
            'total_stock': product.total_stock,
            'stock_sold': product.stock_sold,
            'stock_restocked': product.stock_restocked,
            'available_stock': product.available_stock,
            'location': product.location
        }
    
    def put(self, product_id):
        product = Product.query.get_or_404(product_id)
        data = request.get_json()
        
        # Update product fields
        product.name = data.get('name', product.name)
        product.category = data.get('category', product.category)
        product.product_type = data.get('product_type', product.product_type)
        
        # Parse expiry date if provided
        if data.get('expiry_date'):
            try:
                product.expiry_date = datetime.fromisoformat(data['expiry_date'])
            except ValueError:
                return {'message': 'Invalid expiry date format'}, 400
        
        product.price = data.get('price', product.price)
        product.total_stock = data.get('total_stock', product.total_stock)
        product.stock_sold = data.get('stock_sold', product.stock_sold)
        product.stock_restocked = data.get('stock_restocked', product.stock_restocked)
        product.available_stock = data.get('available_stock', product.available_stock)
        product.location = data.get('location', product.location)
        
        db.session.commit()
        
        return {'message': 'Product updated successfully'}
    
    def delete(self, product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        
        return {'message': 'Product deleted successfully'}