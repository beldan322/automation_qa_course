import time

from pages.Widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


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


    class TestDatePickerPage:

        def test_select_date(self, driver):
            select_date_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            select_date_page.open()
            date = select_date_page.select_date()
            print(date)



        def test_date_and_time(self, driver):
            select_date_and_time_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            select_date_and_time_page.open()
            date = select_date_and_time_page.select_date_and_time()
            print(date)

    class TestSliderPage:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, 'выпало 25, перезапустите тест'


    class TestProgressBarPage:


        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.check_progress_bar_page()
            assert before != after


    class TestTabsPage:

        def test_check_tabs(self, driver):
            tabs_check_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_check_page.open()
            text1, text2, text3 = tabs_check_page.check_text_tabs()
            assert text1 == 574
            assert text2 == 1059
            assert text3 == 613


    class TestToolTips:


        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, input_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button'
            assert input_text == 'You hovered over the text field'
            assert contrary_text == 'You hovered over the Contrary'
            assert section_text == 'You hovered over the 1.10.32'



    class TestMenu:


        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data =  menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »',
                            'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']


