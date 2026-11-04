# pawsswipe_v1/app.py
import os
import requests  # Included intentionally to trigger a second dependency error
from flask import Flask

app = Flask(__name__)

# ==========================================
# TRAP 1: THE ENVIRONMENT VARIABLE TRAP
# Using os.environ[] instead of os.environ.get() intentionally 
# forces a loud KeyError if the variable is not set by the OS.
# ==========================================
DB_URL = os.environ['DATABASE_URL'] 

@app.route('/')
def index():
    # A simple, ugly HTML interface to prove the app is running
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>PawsSwipe v1.0</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f4f4f9; }}
                h1 {{ color: #002864; }}
                .btn {{ padding: 15px 30px; font-size: 20px; background-color: #0089f7; color: white; border: none; border-radius: 8px; cursor: pointer; }}
                .btn:hover {{ background-color: #6dc4ef; }}
                .db-status {{ margin-top: 50px; font-size: 12px; color: #555; }}
            </style>
        </head>
        <body>
            <h1>🐶 Welcome to PawsSwipe 🐶</h1>
            <h2>Find your dog's perfect playdate.</h2>
            <br>
            <button class="btn">Swipe Right</button>
            
            <div class="db-status">
                System Status: Connected to Database at [ {DB_URL} ]
            </div>
        </body>
    </html>
    """
    return html

if __name__ == '__main__':
    print("Starting DumpsterFire Inc. PawsSwipe Server...")
    print("Attempting to bind to port 5000...")
    
    # ==========================================
    # TRAP 2: THE PORT CONFLICT TRAP
    # Port 5000 is notoriously occupied on modern OS (e.g., macOS AirPlay Receiver).
    # Students will be forced to edit this file to change the port to 8080.
    # ==========================================
    app.run(host='0.0.0.0', port=8080)


