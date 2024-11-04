import pytest, requests, os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from endpoints.create_object import CreateBooking, CreateObject
from endpoints.delete_object import DeleteObject
from headers.headers import get_headers
from payloads.payloads import create_booking_payload
from pages.practicetest.practicetest_practice_page import PracticePage
from pages.practicetest.practicetest_main_page import MainPage
from pages.practicetest.practicetest_login_page import LoginPage
from pages.practicetest.practicetest_exceptions_page import ExceptionsPage
load_dotenv()

#Fixtures for API
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
    username = os.getenv("RESTFUL_BOOKER_USERNAME")
    password = os.getenv("RESTFUL_BOOKER_PASSWORD")
    url = 'https://restful-booker.herokuapp.com/auth'
    payload = {
        "username": username,
        "password": password
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
    yield booking_id
    #Post-condition; will be triggered after 'yield' response
    delete_object = DeleteObject()
    delete_object.delete_by_id(booking_id, headers=headers)

#Fixtures for UI e2e
@pytest.fixture(scope='session')
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  # Headless mode off for visibility
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope='session')
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope='session')
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope='session')
def practice_page(page):
    return PracticePage(page)

@pytest.fixture(scope='session')
def main_page(page):
    return MainPage(page)

@pytest.fixture(scope='session')
def login_page(page):
    return LoginPage(page)

@pytest.fixture(scope='session')
def exceptions_page(page):
    return ExceptionsPage(page)

@pytest.fixture
def reload_page(page: Page):
    def _reload_page():
        page.reload()
    return _reload_page