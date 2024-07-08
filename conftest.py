import pytest
import requests
from playwright.sync_api import Page
from endpoints.create_object import CreateBooking, CreateObject
from endpoints.delete_object import DeleteObject
from headers.headers import get_headers
from payloads.payloads import create_booking_payload

@pytest.fixture()
#Pre-condition
def obj_id():
    create_object = CreateObject()
    payload = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
        }
    }

    create_object.new_object(payload)
    yield create_object.response_json['id']
    #Post-condition; will be triggered after 'yield' response
    delete_object = DeleteObject()
    delete_object.delete_by_id(create_object.response_json['id'])

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page

@pytest.fixture(scope='session')
def booking_auth_token():
    url = 'https://restful-booker.herokuapp.com/auth'
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url, json=payload)
    response_json = response.json()
    return response_json['token']

@pytest.fixture(scope='session')
def booking_object_id(booking_auth_token):
    create_object = CreateBooking()
    payload = create_booking_payload()
    headers = get_headers(booking_auth_token)
    create_object.new_booking(payload=payload, headers=headers)
    booking_id = create_object.response_json['bookingid']
    print(booking_id)
    yield booking_id
    #Post-condition; will be triggered after 'yield' response
    delete_object = DeleteObject()
    delete_object.delete_by_id(booking_id, headers=headers)