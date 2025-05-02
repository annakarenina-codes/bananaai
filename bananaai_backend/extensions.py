from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

db = SQLAlchemy()
migrate = Migrate()

# Change this line - don't initialize Api yet
api = None  # We'll initialize this in create_app