import os
import sys
from flask import Flask, send_from_directory
from flask_cors import CORS

# Adjust path for local imports
sys.path.insert(0, os.path.dirname(__file__))

from models.evaluation import db
from routes.evaluation import evaluation_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS
CORS(app)

# Register API blueprint
app.register_blueprint(evaluation_bp, url_prefix='/api')

# REMOVE SQLite setup - it doesn't work on Vercel
# Use environment variable for database URL
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    # Try to create tables
    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        print(f"Database error: {e}")
else:
    print("No DATABASE_URL found - database operations will fail")

# Serve static frontend (optional)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404
