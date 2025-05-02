from flask import request
from flask_restful import Resource
from bananaai_backend.extensions import db
from bananaai_backend.models import InventoryMovement, Product
from datetime import datetime

class InventoryMovementListResource(Resource):
    def get(self):
        movements = InventoryMovement.query.all()
        return [
            {
                'id': movement.id,
                'product_id': movement.product_id,
                'movement_date': movement.movement_date.isoformat(),
                'movement_type': movement.movement_type,
                'quantity': movement.quantity
            } for movement in movements
        ]
    
    def post(self):
        data = request.get_json()
        
        product_id = data.get('product_id')
        movement_type = data.get('movement_type')
        quantity = data.get('quantity', 0)
        
        # Validate the product exists
        product = Product.query.get_or_404(product_id)
        
        # Create movement
        new_movement = InventoryMovement(
            product_id=product_id,
            movement_type=movement_type,
            quantity=quantity
        )
        
        # Update product stock based on movement type
        if movement_type == 'restock':
            product.total_stock += quantity
            product.stock_restocked += quantity
            product.available_stock += quantity
        elif movement_type == 'sell':
            if product.available_stock < quantity:
                return {'message': 'Not enough available stock'}, 400
            product.stock_sold += quantity
            product.available_stock -= quantity
        elif movement_type == 'damage':
            if product.available_stock < quantity:
                return {'message': 'Not enough available stock'}, 400
            product.available_stock -= quantity
        else:
            return {'message': 'Invalid movement type'}, 400
        
        db.session.add(new_movement)
        db.session.commit()
        
        return {
            'message': 'Inventory movement recorded successfully',
            'id': new_movement.id
        }, 201

class InventoryMovementResource(Resource):
    def get(self, movement_id):
        movement = InventoryMovement.query.get_or_404(movement_id)
        
        return {
            'id': movement.id,
            'product_id': movement.product_id,
            'movement_date': movement.movement_date.isoformat(),
            'movement_type': movement.movement_type,
            'quantity': movement.quantity
        }
    
    def delete(self, movement_id):
        movement = InventoryMovement.query.get_or_404(movement_id)
        
        # Revert the inventory changes
        product = Product.query.get(movement.product_id)
        if product:
            if movement.movement_type == 'restock':
                product.total_stock -= movement.quantity
                product.stock_restocked -= movement.quantity
                product.available_stock -= movement.quantity
            elif movement.movement_type == 'sell':
                product.stock_sold -= movement.quantity
                product.available_stock += movement.quantity
            elif movement.movement_type == 'damage':
                product.available_stock += movement.quantity
        
        db.session.delete(movement)
        db.session.commit()
        
        return {'message': 'Inventory movement deleted and stock updated'}