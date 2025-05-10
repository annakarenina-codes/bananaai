from flask import request
from flask_restful import Resource
from bananaai_backend.extensions import db
from bananaai_backend.models import Invoice, InvoiceItem, Product, InventoryMovement
from datetime import datetime

class SaleListResource(Resource):
    def get(self):
        invoices = Invoice.query.all()
        return [
            {
                'id': invoice.id,
                'invoice_number': invoice.invoice_number,
                'issue_date': invoice.issue_date.isoformat(),
                'customer_name': invoice.customer_name,
                'total_amount': invoice.total_amount,
                'status': invoice.status
            } for invoice in invoices
        ]
    
    def post(self):
        data = request.get_json()
        
        # Generate invoice number (simple implementation)
        current_time = datetime.utcnow()
        invoice_number = f"INV-{current_time.strftime('%Y%m%d')}-{current_time.timestamp():.0f}"[-12:]
        
        # Create new invoice
        new_invoice = Invoice(
            invoice_number=invoice_number,
            customer_id=data.get('customer_id'),
            customer_name=data.get('customer_name', 'Guest'),
            total_amount=0,  # Will calculate based on items
            status=data.get('status', 'paid'),
            payment_method=data.get('payment_method', 'cash'),
            due_date=datetime.fromisoformat(data['due_date']) if data.get('due_date') else None
        )
        
        db.session.add(new_invoice)
        db.session.flush()  # Get invoice ID without committing
        
        # Process items
        total_amount = 0
        for item_data in data.get('items', []):
            product_id = item_data['product_id']
            quantity = item_data['quantity']
            
            # Get product
            product = Product.query.get_or_404(product_id)
            
            # Check if enough stock
            if product.available_stock < quantity:
                db.session.rollback()
                return {'message': f'Not enough stock for product {product.name}'}, 400
            
            # Calculate price
            unit_price = product.price
            total_price = unit_price * quantity
            
            # Create invoice item
            invoice_item = InvoiceItem(
                invoice_id=new_invoice.id,
                product_id=product_id,
                quantity=quantity,
                unit_price=unit_price,
                total_price=total_price
            )
            
            # Update product stock
            product.stock_sold += quantity
            product.available_stock -= quantity
            
            # Create inventory movement
            inventory_movement = InventoryMovement(
                product_id=product_id,
                movement_type='sell',
                quantity=quantity
            )
            
            db.session.add(invoice_item)
            db.session.add(inventory_movement)
            
            total_amount += total_price
        
        # Update invoice total
        new_invoice.total_amount = total_amount
        
        db.session.commit()
        
        return {
            'message': 'Sale recorded successfully',
            'invoice_id': new_invoice.id,
            'invoice_number': new_invoice.invoice_number
        }, 201

class SaleResource(Resource):
    def get(self, sale_id):
        invoice = Invoice.query.get_or_404(sale_id)
        
        # Get items
        items = []
        for item in invoice.items:
            product = Product.query.get(item.product_id)
            items.append({
                'id': item.id,
                'product_id': item.product_id,
                'product_name': product.name if product else 'Unknown',
                'quantity': item.quantity,
                'unit_price': item.unit_price,
                'total_price': item.total_price
            })
        
        return {
            'id': invoice.id,
            'invoice_number': invoice.invoice_number,
            'issue_date': invoice.issue_date.isoformat(),
            'customer_id': invoice.customer_id,
            'customer_name': invoice.customer_name,
            'total_amount': invoice.total_amount,
            'status': invoice.status,
            'payment_method': invoice.payment_method,
            'due_date': invoice.due_date.isoformat() if invoice.due_date else None,
            'items': items
         }
    def put(self, sale_id):
        invoice = Invoice.query.get_or_404(sale_id)
        data = request.get_json()

    # Update invoice fields
        invoice.customer_id = data.get('customer_id', invoice.customer_id)
        invoice.customer_name = data.get('customer_name', invoice.customer_name)
        invoice.status = data.get('status', invoice.status)
        invoice.payment_method = data.get('payment_method', invoice.payment_method)

    # If due_date exists, attempt to update it
        if data.get('due_date'):
            try:
                invoice.due_date = datetime.fromisoformat(data['due_date'])
            except ValueError:
                return {'message': 'Invalid date format'}, 400

    # Process each item in the invoice
        for item_data in data.get('items', []):
            product_id = item_data['product_id']
            quantity = item_data['quantity']

        # Get the product
            product = Product.query.get_or_404(product_id)

        # Update the corresponding InventoryMovement
            inventory_movement = InventoryMovement.query.filter_by(
                product_id=product_id,
                movement_type='sell'
            ).first()  # Adjust as per your logic, maybe you want the first matching movement.

            if inventory_movement:
            # Example of updating an existing movement (you can modify it based on your logic)
                inventory_movement.quantity = quantity
                db.session.commit()

        db.session.commit()

        return {'message': 'Sale updated successfully'}
