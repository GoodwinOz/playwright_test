from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.practicetest.locators import LoginPageLocators

class LoginPage(BasePage):
    def type_username(self):
        login_input = self.page.locator(LoginPageLocators.username_input)
        expect(login_input).to_be_visible()
        login_input.fill('student')

    def type_wrong_username(self):
        login_input = self.page.locator(LoginPageLocators.username_input)
        expect(login_input).to_be_visible()
        login_input.fill('student1')

    def type_password(self):
        password_input = self.page.locator(LoginPageLocators.password_input)
        expect(password_input).to_be_visible()
        password_input.fill('Password123')

    def type_wrong_password(self):
        password_input = self.page.locator(LoginPageLocators.password_input)
        expect(password_input).to_be_visible()
        password_input.fill('Password123!')
    
    def click_submit(self):
        submit_button = self.page.locator(LoginPageLocators.submit_button)
        expect(submit_button).to_be_visible()
        submit_button.click()
    
    def verify_log_in_was_successful(self):
        post_title = self.page.locator(LoginPageLocators.logged_in_post_title)
        expect(post_title).to_be_visible()
        expect(post_title).to_contain_text("Logged In Successfully")

    def log_out(self):
        log_out_button = self.page.locator(LoginPageLocators.log_out_button)
        expect(log_out_button).to_be_visible()
        log_out_button.click()
    
    def verify_login_error(self, text):
        login_error = self.page.locator(LoginPageLocators.login_error)
        expect(login_error).to_be_visible()
        expect(login_error).to_contain_text(text)

    