from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from .extensions import db, migrate
from .config import Config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS

# Import resources
from .resources.product import ProductResource, ProductListResource
from .resources.sale import SaleResource, SaleListResource
from .resources.inventory import InventoryMovementResource, InventoryMovementListResource
from .resources.forecast import ForecastResource, ForecastListResource, ProductForecastResource
from .resources.notification import NotificationResource, NotificationListResource, SystemNotificationResource
from .resources.auth import UserRegister, UserLogin


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Setup rate limiting
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["200 per day", "50 per hour"],
        storage_uri="memory://",
    )

    # Setup CORS with appropriate restrictions
    CORS(app, resources={
        r"/*": {
            "origins": app.config.get('ALLOWED_ORIGINS', '*'),
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    
    # Create and initialize the API here
    api = Api(app)
    
    # Import and register models
    with app.app_context():
        from . import models
    

    #Register User API resources
    api.add_resource(UserRegister, '/api/auth/register')
    api.add_resource(UserLogin, '/api/auth/login')

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

    # Apply rate limiting to sensitive endpoints
    limiter.limit("5 per minute")(UserLogin)
    limiter.limit("3 per minute")(UserRegister)    

    # Add debug prints
    print(f"🔍 API Routes registered! Check routes:")
    for rule in app.url_map.iter_rules():
        print(f"  - {rule}")
    
    # Add a simple index route

    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200

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