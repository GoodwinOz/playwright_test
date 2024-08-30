import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Used in perfomace testing; using fixtures throwing error
def get_booking_auth_token():
    username = os.getenv("RESTFUL_BOOKER_USERNAME")
    password = os.getenv("RESTFUL_BOOKER_PASSWORD")
    url = 'https://restful-booker.herokuapp.com/auth'
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=payload)
    response_json = response.json()
    
    if 'token' not in response_json:
        raise ValueError("Response does not contain 'token': " + str(response_json))
    
    return response_json['token']