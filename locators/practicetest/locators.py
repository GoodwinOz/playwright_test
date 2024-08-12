class MainPageLocators:
    practice_button = ".menu-item.menu-item-20.menu-item-object-page.menu-item-type-post_type > a"

class PracticePageLocators:
    test_login_page = ".is-layout-flex.wp-block-columns.wp-block-columns-is-layout-flex.wp-container-core-columns-is-layout-1 > div:nth-of-type(1)  a"

class LoginPageLocators:
    username_input = "#username"
    password_input = "#password"
    submit_button = "#submit"
    logged_in_post_title = ".post-title"
    log_out_button = "#loop-container > div > article > div.post-content > div > div > div > a"
    login_error = "#error"