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
    
    # Register Product API resources
    api.add_resource(ProductListResource, '/api/products')
    api.add_resource(ProductResource, '/api/products/<int:product_id>')
    
    # Register Sale API resources
    api.add_resource(SaleListResource, '/api/sales')
    api.add_resource(SaleResource, '/api/sales/<int:sale_id>')

    # Register Inventory API resources
    api.add_resource(InventoryMovementListResource, '/api/inventory-movements')
    api.add_resource(InventoryMovementResource, '/api/inventory-movements/<int:movement_id>')

    # Register Forecast API resources
    api.add_resource(ForecastListResource, '/api/forecasts')
    api.add_resource(ForecastResource, '/api/forecasts/<int:forecast_id>')
    api.add_resource(ProductForecastResource, '/api/forecasts/product/<int:product_id>')

    # Register Notification API resources
    api.add_resource(NotificationListResource, '/api/notifications')
    api.add_resource(NotificationResource, '/api/notifications/<int:notification_id>')
    api.add_resource(SystemNotificationResource, '/api/system-notifications')

    
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