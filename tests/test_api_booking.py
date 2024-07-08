import requests
import pytest
import allure
from conftest import booking_auth_token
from endpoints.create_object import CreateBooking, CreateObject
from endpoints.get_object import GetBooking
from endpoints.update_object import UpdateBooking
from endpoints.delete_object import  DeleteBooking
from headers.headers import get_headers
from payloads.payloads import create_booking_payload, update_booking_payload
from validators.validators import validate_status_code, validate_response_key

@allure.feature('Booking')
@allure.story('Create Booking')
def test_create_booking():
    payload = create_booking_payload()
    headers = get_headers(booking_auth_token)
    create_booking = CreateBooking()
    create_booking.new_booking(payload=payload, headers=headers)
    validate_status_code(create_booking.response, 200)
    create_booking.check_response_is_200()
    validate_response_key(create_booking.response_json['booking'], 'firstname', payload['firstname'])

@allure.feature('Booking')
@allure.story('Get Booking')
def test_get_booking(booking_object_id, booking_auth_token):
    headers = get_headers(booking_auth_token)
    payload = create_booking_payload()
    get_booking = GetBooking()
    get_booking.get_booking_by_id(booking_object_id, headers=headers)
    get_booking.check_response_is_200()
    validate_response_key(get_booking.response_json, 'firstname', payload['firstname'])
    validate_response_key(get_booking.response_json, 'additionalneeds', payload['additionalneeds'])

@allure.feature('Booking')
@allure.story('Update Booking')
def test_put_booking_obj(booking_object_id, booking_auth_token):
    payload = update_booking_payload()
    headers = get_headers(booking_auth_token)
    update_booking = UpdateBooking()
    update_booking.update_booking_by_id(booking_object_id, payload=payload, headers=headers)
    update_booking.check_response_is_200()
    validate_response_key(update_booking.response_json, 'firstname', payload['firstname'])
    validate_response_key(update_booking.response_json, 'additionalneeds', payload['additionalneeds'])

@allure.feature('Booking')
@allure.story('Delete Booking')
def test_delete_obj(booking_object_id, booking_auth_token):
    headers = get_headers(booking_auth_token)
    delete_booking = DeleteBooking()
    delete_booking.delete_booking_by_id(booking_object_id, headers=headers)
    assert delete_booking.response.status_code == 201
    print(delete_booking.response.text)
    get_booking = GetBooking()
    try:
        get_booking.get_booking_by_id(booking_object_id, headers=headers)
    except requests.exceptions.JSONDecodeError:
        assert get_booking.response.status_code == 404
    else:
        assert False, f"Expected GET request to return 404 status code, but got {get_booking.response.status_code} status code"