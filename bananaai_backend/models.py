from datetime import datetime
from .extensions import db

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    product_type = db.Column(db.String(20))  # perishable/non-perishable
    expiry_date = db.Column(db.Date, nullable=True)
    price = db.Column(db.Float, nullable=False)
    total_stock = db.Column(db.Integer, default=0)
    stock_sold = db.Column(db.Integer, default=0)
    stock_restocked = db.Column(db.Integer, default=0)
    available_stock = db.Column(db.Integer, default=0)
    location = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    inventory_movements = db.relationship('InventoryMovement', backref='product', lazy=True)
    invoice_items = db.relationship('InvoiceItem', backref='product', lazy=True)
    forecasts = db.relationship('Forecast', backref='product', lazy=True)
    
    def __repr__(self):
        return f"<Product {self.name}>"

class InventoryMovement(db.Model):
    __tablename__ = 'inventory_movements'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    movement_date = db.Column(db.DateTime, default=datetime.utcnow)
    movement_type = db.Column(db.String(20))  # restock/sell/damage
    quantity = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<InventoryMovement {self.id} - {self.movement_type}>"

class Forecast(db.Model):
    __tablename__ = 'forecasts'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    predicted_demand = db.Column(db.Integer)
    historical_demand = db.Column(db.Integer)
    forecast_error = db.Column(db.Float)
    confidence_interval_lower = db.Column(db.Float)
    confidence_interval_upper = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Forecast {self.product_id} - {self.date}>"

class Invoice(db.Model):
    __tablename__ = 'invoices'
    
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(20), unique=True)
    issue_date = db.Column(db.DateTime, default=datetime.utcnow)
    customer_id = db.Column(db.String(50))
    customer_name = db.Column(db.String(100))
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='paid')  # paid/unpaid
    payment_method = db.Column(db.String(20), default='cash')  # cash/credit
    due_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    items = db.relationship('InvoiceItem', backref='invoice', lazy=True)
    
    def __repr__(self):
        return f"<Invoice {self.invoice_number}>"

class InvoiceItem(db.Model):
    __tablename__ = 'invoice_items'
    
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"<InvoiceItem {self.id}>"

class Notification(db.Model):
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    notification_type = db.Column(db.String(30))  # low stock, expiry reminder, demand spike
    message = db.Column(db.String(200))
    notification_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10), default='unread')  # unread/read
    recipient_user_id = db.Column(db.String(50))
    
    def __repr__(self):
        return f"<Notification {self.id} - {self.notification_type}>"