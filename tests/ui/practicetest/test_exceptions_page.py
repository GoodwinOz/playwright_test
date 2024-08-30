def test_move_to_practice_page(practice_page):
    practice_page.open()
    practice_page.click_on_practice_button()

def test_move_to_exception_page(exceptions_page):
    exceptions_page.click_on_exceptions_button()
    exceptions_page.verify_exceptions_page_loaded()

#Row 2 validation
def test_add_row_2(exceptions_page):
    exceptions_page.click_on_add_button()
    exceptions_page.verify_confirmation_message("Row 2 was added")

def test_type_text_into_row_2_input(exceptions_page):
    exceptions_page.change_text_in_row_2("Row 2 test 1")
    exceptions_page.click_on_row_2_save_button()
    exceptions_page.verify_confirmation_message("Row 2 was saved")

def test_edit_row_2_message(exceptions_page):
    exceptions_page.click_on_row_2_edit_button()
    exceptions_page.change_text_in_row_2("Row 2 test 2")
    exceptions_page.click_on_row_2_save_button()
    exceptions_page.verify_confirmation_message("Row 2 was saved")

def test_remove_row_2(exceptions_page):
    exceptions_page.click_on_row_2_remove_button()
    exceptions_page.verify_confirmation_message("Row 2 was removed")
    
#Row 1 validation
def test_edit_row_1_message(exceptions_page):
    exceptions_page.click_on_row_1_edit_button()
    exceptions_page.change_text_in_row_1("Row 1 test 1")
    exceptions_page.click_on_row_1_save_button()
    exceptions_page.verify_confirmation_message("Row 1 was saved")

def test_verify_row_1_message_after_page_reload(exceptions_page, reload_page):
    reload_page()
    exceptions_page.click_on_row_1_edit_button()
    exceptions_page.change_text_in_row_1("Row 1 test 2")
    exceptions_page.click_on_row_1_save_button()
    exceptions_page.verify_confirmation_message("Row 1 was saved")

def test_verify_row_1_message_after_adding_row_2(exceptions_page):
    exceptions_page.click_on_add_button()
    exceptions_page.change_text_in_row_2("Row 2 test 3")
    exceptions_page.click_on_row_2_save_button()
    exceptions_page.verify_confirmation_message("Row 2 was saved")
    exceptions_page.verify_text_in_row_1("Row 1 test 2")