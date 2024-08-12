from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.practicetest.locators import MainPageLocators

class MainPage(BasePage):
    url = "https://practicetestautomation.com/"

    def verify_page_is_loaded(self):
        practice_button = self.page.locator(MainPageLocators.practice_button)
        expect(practice_button).to_be_visible()
        expect(self.page).to_have_title("Practice Test Automation | Learn Selenium WebDriver")