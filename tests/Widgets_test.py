import time

from pages.Widgets_page import AccordianPage, AutoCompletePage


class TestWidgetsPage:
    class TestAccordianPage:


        def test_check_text_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_text, second_text, third_text = accordian_page.check_accordian_text()
            assert first_text == 574
            assert second_text == 763
            assert third_text == 613



    class TestAutoCompletePage:


        def test_multiple_color_names(self, driver):
            multiple_color = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            multiple_color.open()
            colors = multiple_color.fill_multi_input()
            time.sleep(4)
            colors_result = multiple_color.check_multi()
            assert colors == colors_result

        def test_remove_value_multi_color(self, driver):
            multiple_color = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            multiple_color.open()
            multiple_color.fill_multi_input()
            before_value, after_value = multiple_color.delete_multi_color()
            assert before_value != after_value



        def test_single_color_name(self, driver):
            single_color = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            single_color.open()
            before_color, after_color = single_color.single_color_check()
            assert before_color == after_color
