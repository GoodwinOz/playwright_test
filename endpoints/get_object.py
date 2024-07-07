import requests
from endpoints.base_endpoint import Endpoint

class GetObject(Endpoint):

    def get_by_id(self, object_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()

class GetBooking(Endpoint):

    def get_booking_by_id(self, object_id, headers):
        self.response = requests.get(f'https://restful-booker.herokuapp.com/booking/{object_id}', headers=headers)
        self.response_json = self.response.json()