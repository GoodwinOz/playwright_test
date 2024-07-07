import requests
from endpoints.base_endpoint import Endpoint

class DeleteObject(Endpoint):
    
    def delete_by_id(self, object_id, headers=None):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()

class DeleteBooking(Endpoint):

    def delete_booking_by_id(self, object_id, headers=None):
        self.response = requests.delete(f'https://restful-booker.herokuapp.com/booking/{object_id}', headers=headers)
        if self.response.status_code != 201:
            self.response.raise_for_status()
        else:
            self.response_json = {'message': self.response.text}