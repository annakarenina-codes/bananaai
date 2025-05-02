from flask import Flask, jsonify
from flask_restful import Api
from .extensions import db, migrate
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Create and initialize the API here
    api = Api(app)
    
    # Import and register models
    with app.app_context():
        from . import models
    
    # Import resources
    from .resources.product import ProductResource, ProductListResource
    from .resources.sale import SaleResource, SaleListResource
    from .resources.inventory import InventoryMovementResource, InventoryMovementListResource
    from .resources.forecast import ForecastResource, ForecastListResource, ProductForecastResource
    from .resources.notification import NotificationResource, NotificationListResource, SystemNotificationResource
    
    # Register API resources
    api.add_resource(ProductListResource, '/api/products')
    api.add_resource(ProductResource, '/api/products/<int:product_id>')
    
    # ... rest of your resource registrations ...
    
    # Add debug prints
    print(f"🔍 API Routes registered! Check routes:")
    for rule in app.url_map.iter_rules():
        print(f"  - {rule}")
    
    # Add a simple index route
    @app.route('/')
    def index():
        return {
            'name': 'BananaAI Backend API',
            'version': '1.0.0',
            'status': 'running'
        }
    
    # Add a debug route
    @app.route('/debug')
    def debug_route():
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append({
                'endpoint': rule.endpoint,
                'methods': list(rule.methods),
                'path': str(rule)
            })
        
        return jsonify({
            'message': 'Debug route working',
            'registered_routes': routes,
            'total_routes': len(routes)
        })
    
    return app