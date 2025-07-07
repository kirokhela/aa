import os
import sys

from flask import Flask, send_from_directory
from flask_cors import CORS
from models.evaluation import create_evaluation_table
from routes.evaluation import evaluation_bp

# --- Configuration ---
PORT = 7020
STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')
SECRET_KEY = 'asdf#FGSgvasgf$5$WGT'

# --- Create Flask app ---
app = Flask(__name__, static_folder=STATIC_FOLDER)
app.config['SECRET_KEY'] = SECRET_KEY
CORS(app)

# --- Initialize DB ---
create_evaluation_table()

# --- Register routes ---
app.register_blueprint(evaluation_bp, url_prefix='/api')

# --- Serve static HTML ---


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    full_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(full_path):
        return send_from_directory(app.static_folder, path)
    elif os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return send_from_directory(app.static_folder, 'index.html')
    else:
        return "index.html not found", 404

