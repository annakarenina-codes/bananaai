#setup_data.py
import os
import datetime
from flask import Flask
from bananaai_backend import create_app
from bananaai_backend.extensions import db
from bananaai_backend.models import Product, InventoryMovement, Invoice, InvoiceItem, Notification

def create_test_data():
    """Create initial test data for development"""
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.session.query(InvoiceItem).delete()
        db.session.query(Invoice).delete()
        db.session.query(InventoryMovement).delete()
        db.session.query(Notification).delete()
        db.session.query(Product).delete()
        db.session.commit()
        
        # Create products
        products = [
            Product(
                name="Cavendish Banana",
                category="Fruits",
                product_type="perishable",
                expiry_date=datetime.datetime.utcnow().date() + datetime.timedelta(days=5),
                price=0.99,
                total_stock=100,
                stock_sold=0,
                stock_restocked=100,
                available_stock=100,
                location="Section A"
            ),
            Product(
                name="Red Banana",
                category="Fruits",
                product_type="perishable",
                expiry_date=datetime.datetime.utcnow().date() + datetime.timedelta(days=4),
                price=1.29,
                total_stock=50,
                stock_sold=0,
                stock_restocked=50,
                available_stock=50,
                location="Section A"
            ),
            Product(
                name="Plantain",
                category="Fruits",
                product_type="perishable",
                expiry_date=datetime.datetime.utcnow().date() + datetime.timedelta(days=7),
                price=1.49,
                total_stock=75,
                stock_sold=0,
                stock_restocked=75,
                available_stock=75,
                location="Section B"
            ),
            Product(
                name="Banana Chips",
                category="Snacks",
                product_type="non-perishable",
                expiry_date=datetime.datetime.utcnow().date() + datetime.timedelta(days=180),
                price=3.99,
                total_stock=30,
                stock_sold=0,
                stock_restocked=30,
                available_stock=30,
                location="Section C"
            ),
            Product(
                name="Banana Bread Mix",
                category="Bakery",
                product_type="non-perishable",
                expiry_date=datetime.datetime.utcnow().date() + datetime.timedelta(days=120),
                price=4.99,
                total_stock=20,
                stock_sold=0,
                stock_restocked=20,
                available_stock=20,
                location="Section D"
            ),
        ]
        
        for product in products:
            db.session.add(product)
        
        db.session.commit()
        print(f"Created {len(products)} products")
        
        # Create some inventory movements
        for product in products:
            movement = InventoryMovement(
                product_id=product.id,
                movement_type="restock",
                quantity=product.total_stock
            )
            db.session.add(movement)
        
        db.session.commit()
        print("Created initial inventory movements")
        
        # Create an invoice with items
        invoice = Invoice(
            invoice_number="INV-20250501-001",
            customer_name="Test Customer",
            total_amount=0,
            status="paid",
            payment_method="cash"
        )
        db.session.add(invoice)
        db.session.flush()
        
        # Add items to invoice
        item1 = InvoiceItem(
            invoice_id=invoice.id,
            product_id=products[0].id,
            quantity=5,
            unit_price=products[0].price,
            total_price=products[0].price * 5
        )
        
        item2 = InvoiceItem(
            invoice_id=invoice.id,
            product_id=products[1].id,
            quantity=3,
            unit_price=products[1].price,
            total_price=products[1].price * 3
        )
        
        db.session.add(item1)
        db.session.add(item2)
        
        # Update invoice total
        invoice.total_amount = item1.total_price + item2.total_price
        
        # Update product stocks
        products[0].stock_sold = 5
        products[0].available_stock -= 5
        products[1].stock_sold = 3
        products[1].available_stock -= 3
        
        # Create corresponding inventory movements
        movement1 = InventoryMovement(
            product_id=products[0].id,
            movement_type="sell",
            quantity=5
        )
        
        movement2 = InventoryMovement(
            product_id=products[1].id,
            movement_type="sell",
            quantity=3
        )
        
        db.session.add(movement1)
        db.session.add(movement2)
        
        # Create a few notifications
        notification1 = Notification(
            notification_type="low_stock",
            message="Low stock alert: Banana Bread Mix has only 20 units left",
            status="unread",
            recipient_user_id="admin"
        )
        
        notification2 = Notification(
            notification_type="expiry_reminder",
            message="Expiry alert: Red Banana will expire in 4 days",
            status="unread",
            recipient_user_id="admin"
        )
        
        db.session.add(notification1)
        db.session.add(notification2)
        
        db.session.commit()
        print("Created test invoice, items, and notifications")
        
        print("Test data setup complete!")

if __name__ == "__main__":
    create_test_data()