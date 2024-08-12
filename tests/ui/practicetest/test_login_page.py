from playwright.sync_api import Page

def test_move_to_practice_page(practice_page):
        practice_page.open()
        practice_page.click_on_practice_button()

def test_move_to_test_login_page(practice_page):
        practice_page.click_on_test_login_button()
        practice_page.verify_test_login_page_is_loaded()

#Login scenario
def test_login_as_student(login_page):
        login_page.type_username()
        login_page.type_password()
        login_page.click_submit()

def test_verify_login_successful(login_page):
        login_page.verify_log_in_was_successful()

def test_log_out(login_page):
        login_page.log_out()

def test_verify_test_login_page_loaded(practice_page):
        practice_page.verify_test_login_page_is_loaded()

#Negative login scenario (wrong login credentials) and login error validation
def test_login_with_wrong_username(login_page):
        login_page.type_wrong_username()
        login_page.type_password()
        login_page.click_submit()

def test_verify_wrong_username_error(login_page):
        login_page.verify_login_error("Your username is invalid!")

def test_login_with_wrong_password(login_page):
        login_page.type_username()
        login_page.type_wrong_password()
        login_page.click_submit()

def test_verify_wrong_password_error(login_page):
        login_page.verify_login_error("Your password is invalid!")
