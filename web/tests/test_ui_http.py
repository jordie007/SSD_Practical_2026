import requests
import subprocess
import time
import os

def test_valid_password():
    process = subprocess.Popen(
        ["python", "app.py"],
        cwd=os.getcwd(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    time.sleep(4)
    
    try:
        strong_pass = "MySuperSecurePass12345!"
        response = requests.post("http://localhost:5000", 
                            data={"password": strong_pass}, 
                            allow_redirects=True, 
                            timeout=5)
        assert response.status_code == 200
        assert "Welcome" in response.text
    finally:
        process.terminate()