import random
import time
from pages.elements_page import TextBoxPage, RadioButtonPage, WebTablePage


class TestsElements:
    class TestTextBox:


        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_fields_form()
            assert full_name == output_name, 'the full name does not match'
            assert email == output_email, 'the email does not match'
            assert current_address == output_current_address, 'the current address does not match'
            assert permanent_address == output_permanent_address, 'the permanent address does not match'
            time.sleep(4)



    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.out_put_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.out_put_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.out_put_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"




    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.chek_new_person()
            assert new_person in table_result, 'нет в таблице'

        def test_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()

            new_person = web_table_page.add_new_person()
            search_text = new_person[1]
            web_table_page.search_person_in_table(search_text)
            result = web_table_page.get_table_rows()
            assert len(result) == 1, f"После поиска должно остаться 1 строка, а осталось: {len(result)}"
            actual_row = result[0]
            expected_row = [cell.strip() for cell in actual_row[:len(new_person)]]
            assert expected_row == new_person, f"Не совпадает строка после поиска: {expected_row} vs {new_person}"