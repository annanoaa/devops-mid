import requests
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='health_check.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def check_app_health(url="http://localhost:5000"):
    """
    Check if the application is running and log the result
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            status = "HEALTHY"
            message = f"Application is running. Status code: {response.status_code}"
        else:
            status = "DEGRADED"
            message = f"Application returned status code: {response.status_code}"
    except requests.RequestException as e:
        status = "DOWN"
        message = f"Application is not accessible: {str(e)}"
    
    # Log the health check result
    log_message = f"[{status}] {message}"
    logging.info(log_message)
    print(log_message)
    
    return status == "HEALTHY"

if __name__ == "__main__":
    check_app_health() 