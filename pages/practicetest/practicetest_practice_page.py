from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.practicetest.locators import MainPageLocators, PracticePageLocators

class PracticePage(BasePage):
    url = "https://practicetestautomation.com/"

    def click_on_practice_button(self):
        practice_button = self.page.locator(MainPageLocators.practice_button)
        expect(practice_button).to_be_visible()
        practice_button.click()

    def click_on_test_login_button(self):
        test_login_button = self.page.locator(PracticePageLocators.test_login_page)
        test_login_button.click()

    def verify_test_login_page_is_loaded(self):
        expect(self.page).to_have_title("Test Login | Practice Test Automation")