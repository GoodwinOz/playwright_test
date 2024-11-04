from playwright.sync_api import Page
from pages.practicetest.practicetest_main_page import MainPage

def test_verify_page_can_be_loaded(page: Page):
        main_page = MainPage(page)
        main_page.open()
        main_page.verify_page_is_loaded()