from flask import request
from flask_restful import Resource
from bananaai_backend.extensions import db
from bananaai_backend.models import Notification, Product
from datetime import datetime, timedelta

class NotificationListResource(Resource):
    def get(self):
        status = request.args.get('status', None)
        
        if status:
            notifications = Notification.query.filter_by(status=status).all()
        else:
            notifications = Notification.query.all()
            
        return [
            {
                'id': notification.id,
                'notification_type': notification.notification_type,
                'message': notification.message,
                'notification_date': notification.notification_date.isoformat(),
                'status': notification.status,
                'recipient_user_id': notification.recipient_user_id
            } for notification in notifications
        ]
    
    def post(self):
        data = request.get_json()
        
        new_notification = Notification(
            notification_type=data.get('notification_type'),
            message=data.get('message'),
            status=data.get('status', 'unread'),
            recipient_user_id=data.get('recipient_user_id')
        )
        
        db.session.add(new_notification)
        db.session.commit()
        
        return {
            'message': 'Notification created successfully',
            'id': new_notification.id
        }, 201

class NotificationResource(Resource):
    def get(self, notification_id):
        notification = Notification.query.get_or_404(notification_id)
        
        return {
            'id': notification.id,
            'notification_type': notification.notification_type,
            'message': notification.message,
            'notification_date': notification.notification_date.isoformat(),
            'status': notification.status,
            'recipient_user_id': notification.recipient_user_id
        }
    
    def put(self, notification_id):
        notification = Notification.query.get_or_404(notification_id)
        data = request.get_json()
        
        notification.status = data.get('status', notification.status)
        
        db.session.commit()
        
        return {'message': 'Notification updated successfully'}
    
    def delete(self, notification_id):
        notification = Notification.query.get_or_404(notification_id)
        db.session.delete(notification)
        db.session.commit()
        
        return {'message': 'Notification deleted successfully'}

class SystemNotificationResource(Resource):
    def post(self):
        """Generate system notifications for low stock and expiring products"""
        # Check for low stock
        low_stock_threshold = 10  # Example threshold
        low_stock_products = Product.query.filter(Product.available_stock <= low_stock_threshold).all()
        
        notifications_created = 0
        
        for product in low_stock_products:
            # Check if a notification already exists for this product
            existing = Notification.query.filter_by(
                notification_type='low_stock',
                message=f"Low stock alert: {product.name} has only {product.available_stock} units left",
                status='unread'
            ).first()
            
            if not existing:
                notification = Notification(
                    notification_type='low_stock',
                    message=f"Low stock alert: {product.name} has only {product.available_stock} units left",
                    status='unread',
                    recipient_user_id='admin'  # Default recipient
                )
                db.session.add(notification)
                notifications_created += 1
        
        # Check for expiring products (within next 7 days)
        today = datetime.utcnow().date()
        expiry_threshold = today + timedelta(days=7)
        
        expiring_products = Product.query.filter(
            Product.product_type == 'perishable',
            Product.expiry_date <= expiry_threshold,
            Product.expiry_date >= today
        ).all()
        
        for product in expiring_products:
            days_to_expiry = (product.expiry_date - today).days
            
            # Check if a notification already exists for this product
            existing = Notification.query.filter_by(
                notification_type='expiry_reminder',
                message=f"Expiry alert: {product.name} will expire in {days_to_expiry} days",
                status='unread'
            ).first()
            
            if not existing:
                notification = Notification(
                    notification_type='expiry_reminder',
                    message=f"Expiry alert: {product.name} will expire in {days_to_expiry} days",
                    status='unread',
                    recipient_user_id='admin'  # Default recipient
                )
                db.session.add(notification)
                notifications_created += 1
        
        db.session.commit()
        
        return {
            'message': 'System notifications generated',
            'notifications_created': notifications_created
        }