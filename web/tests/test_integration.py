import requests
import subprocess
import time
import os

def test_home_page_loads():
    # Ensure we're in the web directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Start the Flask app
    process = subprocess.Popen(
        ["python", "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    time.sleep(5)  # Increased wait time
    
    try:
        response = requests.get("http://localhost:5000", timeout=10)  # Use 5000 as per app.py
        assert response.status_code == 200
        print("Home page loaded successfully")
    finally:
        process.terminate()
        process.wait()