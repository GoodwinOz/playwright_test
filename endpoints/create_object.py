import requests
from endpoints.base_endpoint import Endpoint

class CreateObject(Endpoint):
    
    def new_object(self, payload):
        self.response = requests.post('https://api.restful-api.dev/objects', json = payload)
        self.response_json = self._safe_json()

    def check_response_name(self, name):
        assert self.response_json['name'] == name

class CreateBooking(Endpoint):
    def new_booking(self, payload, headers):
        self.response = requests.post('https://restful-booker.herokuapp.com/booking', json = payload, headers=headers)
        self.response_json = self._safe_json()
    
    def check_response_firstname(self, firstname):
        assert self.response_json['booking']['firstname'] == firstname