import requests
from endpoints.base_endpoint import Endpoint

class UpdateObject(Endpoint):

    def update_by_id(self, object_id, payload):
        self.response = requests.put(
            f'https://api.restful-api.dev/objects/{object_id}',
            json = payload
        )
        self.response_json = self.response.json()

    def check_response_name(self, name):
        assert self.response_json['name'] == name

class UpdateBooking(Endpoint):

    def update_booking_by_id(self, object_id, payload, headers):
        self.response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{object_id}',
            json = payload,
            headers=headers
        )
        self.response_json = self.response.json()

    def check_response_firstname(self, firstname):
        assert self.response_json['firstname'] == firstname