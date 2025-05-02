# app.py
from bananaai_backend import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting BananaAI API server...")
    print("Try accessing: http://localhost:5000/api/products")
    app.run(debug=True)