from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.practicetest.locators import ExceptionsPageLocators, PracticePageLocators

class ExceptionsPage(BasePage):
    url = "https://practicetestautomation.com/"

    def click_on_exceptions_button(self):
        exceptions_button = self.page.locator(PracticePageLocators.exceptions_page)
        exceptions_button.click()

    def verify_exceptions_page_loaded(self):
        expect(self.page).to_have_title("Test Exceptions | Practice Test Automation")

    def click_on_add_button(self):
        add_button = self.page.locator(ExceptionsPageLocators.row_1_add_button)
        add_button.click()

    def verify_row_2_is_visible(self):
        row_2_input = self.page.locator(ExceptionsPageLocators.row_2_input_field)
        expect(row_2_input).to_be_visible()

    def verify_confirmation_message(self, text):
        confirmation_message = self.page.locator(ExceptionsPageLocators.confirmation_message)
        expect(confirmation_message).to_have_text(text)

    def click_on_row_1_save_button(self):
        row_1_save_button = self.page.locator(ExceptionsPageLocators.row_1_save_button)
        row_1_save_button.click()

    def click_on_row_2_save_button(self):
        row_2_save_button = self.page.locator(ExceptionsPageLocators.row_2_save_button)
        row_2_save_button.click()

    def click_on_row_1_edit_button(self):
        row_1_save_button = self.page.locator(ExceptionsPageLocators.row_1_edit_button)
        row_1_save_button.click()

    def click_on_row_2_edit_button(self):
        row_2_save_button = self.page.locator(ExceptionsPageLocators.row_2_edit_button)
        row_2_save_button.click()

    def click_on_row_2_remove_button(self):
        row_2_remove_button = self.page.locator(ExceptionsPageLocators.row_2_remove_button)
        row_2_remove_button.click()

    def change_text_in_row_1(self, text):
        row_1_input_field = self.page.locator(ExceptionsPageLocators.row_1_input_field)
        row_1_input_field.fill(text)
    
    def change_text_in_row_2(self, text):
        row_2_input_field = self.page.locator(ExceptionsPageLocators.row_2_input_field)
        row_2_input_field.fill(text)

    def verify_text_in_row_1(self, text):
        row_1_input_field_value = self.page.locator(ExceptionsPageLocators.row_1_input_field_value)
        expect(row_1_input_field_value).to_have_value(text)