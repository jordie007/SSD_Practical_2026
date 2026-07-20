import requests
import subprocess
import time
import os

def test_home_page_loads():
    # Start the Flask app in background
    process = subprocess.Popen(
        ["python", "app.py"],
        cwd=os.getcwd(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    time.sleep(4)  # Give time for server to start
    
    try:
        response = requests.get("http://localhost:8000", timeout=5)
        assert response.status_code == 200
        assert "password" in response.text.lower() or "Login" in response.text
    finally:
        process.terminate()