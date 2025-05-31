from flask import current_app

class SecurityMiddleware:
    """
    Middleware to add security headers to all responses
    """
    def __init__(self, app):
        self.app = app
        
        # Register after_request handler
        app.after_request(self.add_security_headers)
        
    def add_security_headers(self, response):
        """Add security headers to the response"""
        security_headers = current_app.config.get('SECURITY_HEADERS', {})
        
        for header, value in security_headers.items():
            response.headers[header] = value
            
        return response