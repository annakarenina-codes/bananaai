from .extensions import db

def get_session():
    return db.session