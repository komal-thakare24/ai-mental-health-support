from flask import Flask
from flask_cors import CORS
from routes.screening import screening_routes

app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(screening_routes)

@app.route('/')
def home():
    return "Welcome to the AI-Enabled Mental Health Screening and Support System"

if __name__ == '__main__':
    app.run(debug=True)