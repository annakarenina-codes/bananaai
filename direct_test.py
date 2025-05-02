# direct_test.py
from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Define a simple resource
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello from direct test API!"}

# Register the resource
api.add_resource(HelloResource, '/api/hello')

# Add a regular Flask route
@app.route('/')
def index():
    return jsonify({"message": "Direct test index working"})

if __name__ == '__main__':
    # Print all routes
    print("Routes in direct test:")
    for rule in app.url_map.iter_rules():
        print(f"  - {rule}")
    
    # Run the app
    app.run(debug=True, port=5002)