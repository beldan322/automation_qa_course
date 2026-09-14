import time

from pages.elements_page import TextBoxPage


def test_text_box(driver):
    text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    text_box_page.open()
    full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
    output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_fields_form()
    assert full_name == output_name, 'the full name does not match'
    assert email == output_email, 'the email does not match'
    assert current_address == output_current_address, 'the current address does not match'
    assert permanent_address == output_permanent_address, 'the permanent address does not match'


class TestsElements:
    class TextBoxPage:
        pass


# def test(driver):
#     page = BasePage(driver, 'https://google.com')
#     page.open()
#     time.sleep(3)