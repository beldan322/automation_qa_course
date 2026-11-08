import time

import allure

from pages.Widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage

@allure.suite('Группа "Widgets"')
class TestWidgetsPage:

    @allure.feature('Подгруппа "Accordian"')
    class TestAccordianPage:

        @allure.title('Тест "Check text accordian"')
        def test_check_text_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_text, second_text, third_text = accordian_page.check_accordian_text()
            assert first_text == 574
            assert second_text == 763
            assert third_text == 613

    @allure.feature('Подгруппа "AutoComplete"')
    class TestAutoCompletePage:

        @allure.title('Тест "Check multiple color names"')
        def test_multiple_color_names(self, driver):
            multiple_color = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            multiple_color.open()
            colors = multiple_color.fill_multi_input()
            time.sleep(4)
            colors_result = multiple_color.check_multi()
            assert colors == colors_result

        @allure.title('Тест "Check remove value multi color"')
        def test_remove_value_multi_color(self, driver):
            multiple_color = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            multiple_color.open()
            multiple_color.fill_multi_input()
            before_value, after_value = multiple_color.delete_multi_color()
            assert before_value != after_value

        @allure.title('Тест "Check single color name"')
        def test_single_color_name(self, driver):
            single_color = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            single_color.open()
            before_color, after_color = single_color.single_color_check()
            assert before_color == after_color

    @allure.feature('Подгруппа "DatePicker"')
    class TestDatePickerPage:

        @allure.title('Тест "Check select date"')
        def test_select_date(self, driver):
            select_date_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            select_date_page.open()
            date = select_date_page.select_date()
            print(date)

        @allure.title('Тест "Check date and time"')
        def test_date_and_time(self, driver):
            select_date_and_time_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            select_date_and_time_page.open()
            date = select_date_and_time_page.select_date_and_time()
            print(date)

    @allure.feature('Подгруппа "Slider"')
    class TestSliderPage:

        @allure.title('Тест "Check slider"')
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, 'выпало 25, перезапустите тест'

    @allure.feature('Подгруппа "Progress Bar"')
    class TestProgressBarPage:

        @allure.title('Тест "Check progress bar"')
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.check_progress_bar_page()
            assert before != after

    @allure.feature('Подгруппа "Tabs"')
    class TestTabsPage:

        @allure.title('Тест "Check tabs"')
        def test_check_tabs(self, driver):
            tabs_check_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_check_page.open()
            text1, text2, text3 = tabs_check_page.check_text_tabs()
            assert text1 == 574
            assert text2 == 1059
            assert text3 == 613

    @allure.feature('Подгруппа "ToolTips"')
    class TestToolTipsPage:

        @allure.title('Тест "Check tool tips"')
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, input_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button'
            assert input_text == 'You hovered over the text field'
            assert contrary_text == 'You hovered over the Contrary'
            assert section_text == 'You hovered over the 1.10.32'

    @allure.feature('Подгруппа "Menu"')
    class TestMenuPage:

        @allure.title('Тест "Check menu"')
        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data =  menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »',
                            'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']

    @allure.feature('Подгруппа "Select Menu"')
    class TestSelectMenuPage:

        @allure.title('Тест "Check select value"')# не разобрался с этими селекторам, душная хрень, сделал генератор, вписываю значение из массива и проверяю на неравенство плэйсхолдеру
        def test_select_value(self, driver):
            select_value_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_value_page.open()
            before, after = select_value_page.select_value()
            assert before != after, 'вы ничо не вписали'

        @allure.title('Тест "Check select one"')
        def test_select_one(self, driver):
            select_one_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_one_page.open()
            before, after = select_one_page.select_one()
            assert before != after, 'вы ничо не вписали'

        @allure.title('Тест "Check old style select menu"')
        def test_old_style_select_menu(self, driver):
            old_style_select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            old_style_select_menu_page.open()
            before, after = old_style_select_menu_page.old_style_select_menu()
            assert before != after

        @allure.title('Тест "Check multiselect drop down"')
        def test_multiselect_drop_down(self, driver):
            multiselect_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            multiselect_page.open()
            before, after = multiselect_page.multiselect_drop_down()
            assert before != after





























