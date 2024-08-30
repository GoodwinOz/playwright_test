class MainPageLocators:
    practice_button = ".menu-item.menu-item-20.menu-item-object-page.menu-item-type-post_type > a"

class PracticePageLocators:
    test_login_page = ".is-layout-flex.wp-block-columns.wp-block-columns-is-layout-flex.wp-container-core-columns-is-layout-1 > div:nth-of-type(1)  a"
    exceptions_page = ".is-layout-flex.wp-block-columns.wp-block-columns-is-layout-flex.wp-container-core-columns-is-layout-2 > div:nth-of-type(1)  a"

class LoginPageLocators:
    username_input = "#username"
    password_input = "#password"
    submit_button = "#submit"
    logged_in_post_title = ".post-title"
    log_out_button = "#loop-container > div > article > div.post-content > div > div > div > a"
    login_error = "#error"

class ExceptionsPageLocators:
    row_1_edit_button = "#rows > div:nth-of-type(1) [name='Edit']"
    row_2_edit_button = "div:nth-of-type(3) > .row > button#edit_btn"
    row_1_add_button = "button#add_btn"
    row_1_save_button = "#rows > div:nth-of-type(1) [name='Save']"
    row_2_save_button = "div:nth-of-type(3) > .row > button#save_btn"
    row_1_input_field = "div#row1 > .input-field"
    row_2_input_field = "div#row2 > .input-field"
    row_2_remove_button = "button#remove_btn"
    confirmation_message = "div#confirmation"
    row_1_input_field_value = "div:nth-of-type(1) > .row > .input-field"