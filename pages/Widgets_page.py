import random
import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date, generated_time, generated_value, generated_one_value, \
    generated_four_color
from locators.Widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsLocators, MenuPageLocators, \
    SelectMenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step('Проверка "Accordian"')
    def check_accordian_text(self):
        self.element_is_visible(self.locators.SECTION_FIRST).click()
        first_text = self.element_is_present(self.locators.SECTION_FIRST_TEXT).text
        self.element_is_visible(self.locators.SECTION_SECOND).click()
        second_text = self.element_is_present(self.locators.SECTION_SECOND_TEXT).text
        self.element_is_visible(self.locators.SECTION_THIRD).click()
        third_text = self.element_is_present(self.locators.SECTION_THIRD_TEXT).text
        return len(first_text), len(second_text), len(third_text)


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.step('Проверка автозаполнения цветов')
    def fill_multi_input(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
        for color in colors:
            input_multi.send_keys(Keys.ENTER) #работает и пофиг, я полчаса убил на решение проблемы, без энтера вначале он скипал цвета и даже увеличение таймаута в basepage не помогло
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('Проверка удаления цветов')
    def delete_multi_color(self):
        before_value = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.DELETE_MULTI_VALUE)
        for value in remove_button_list:
            value.click()
            break
        after_value = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return before_value, after_value

    @allure.step('Проверка цветов, которые в поле')
    def check_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors=[]
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step('Проверка заполнения поля с вводом одного цвета')
    def single_color_check(self):
        single = []
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_visible(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        single_result = self.element_is_present(self.locators.SINGLE_VALUE)
        single.append(single_result.text)
        return color, single


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step('Проверка даты')
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_day_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('Проверка текста даты')
    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step('Проверка списка дней')
    def select_day_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for i in item_list:
            if i.text ==  value:
                i.click()
                break

    @allure.step('Проверка заполнения даты и времени')
    def select_date_and_time(self):
        date = next(generated_date())
        time1 = generated_time()
        input_date = self.element_is_visible(self.locators.TIME_AND_DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.TIME_AND_DATE_MONTH).click()
        self.select_day_from_list(self.locators.MONTH_DROPDOWN, date.month)
        self.element_is_clickable(self.locators.TIME_AND_DATE_YEAR).click()
        self.select_day_from_list(self.locators.YEAR_DROPDOWN, '2020')
        self.select_day_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.select_day_from_list(self.locators.TIME_DROPDOWN, time1)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step('Проверка значения ползунка')
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drug_and_drop_by_offset(slider_input, random.randint(1, 99), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after





class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step('Проверка значения шкалы загрузки')
    def check_progress_bar_page(self):
        value_before = self.element_is_present(self.locators.VALUE_BAR).text
        bar_button = self.element_is_visible(self.locators.START_BUTTON)
        bar_button.click()
        time.sleep(random.randint(1,9))
        bar_button.click()
        value_after = self.element_is_present(self.locators.VALUE_BAR).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step('Проверка текста вкладки')
    def check_text_tabs(self):
        self.element_is_visible(self.locators.WHAT_TABS).click()
        text1 = self.element_is_visible(self.locators.TEXT_WHAT_TAB).text
        self.element_is_visible(self.locators.ORIGIN_TABS).click()
        text2 = self.element_is_visible(self.locators.TEXT_ORIGIN_TAB).text
        self.element_is_visible(self.locators.USE_TABS).click()
        text3 = self.element_is_visible(self.locators.TEXT_USE_TAB).text
        return len(text1), len(text2), len(text3)



class ToolTipsPage(BasePage):
    locators = ToolTipsLocators()

    @allure.step('Взятие текста из подсказок')
    def get_text_from_tool_tips(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        self.element_is_visible(wait_element)
        time.sleep(0.3)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIP_INNERS)
        text = tool_tip_text.text
        return text

    @allure.step('Проверка подсказок')
    def check_tool_tips(self):
        tool_tips_text_button = self.get_text_from_tool_tips(self.locators.BOTTON_HOVER, self.locators.TOOL_TIP_BUTTON)
        time.sleep(0.3)
        tool_tips_text_input = self.get_text_from_tool_tips(self.locators.INPUT_HOVER, self.locators.TOOL_TIP_INPUT)
        time.sleep(0.3)
        tool_tips_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_HOVER, self.locators.TOOL_TIP_CONTRARY)
        time.sleep(0.3)
        tool_tips_text_section = self.get_text_from_tool_tips(self.locators.SECTION_HOVER, self.locators.TOOL_TIP_SECTION)
        time.sleep(0.3)
        return tool_tips_text_button, tool_tips_text_input, tool_tips_text_contrary, tool_tips_text_section



class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step('Проверка меню')
    def check_menu(self):
        menu_list = self.elements_are_present(self.locators.MENU_LIST)
        data = []
        for item in menu_list:
            self.action_move_to_element(item)
            time.sleep(0.2)
            data.append(item.text)
        return data



class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    @allure.step('Выбор значений в работе с меню')
    def select_value(self):
        before = self.element_is_visible(self.locators.SELECT_VALUE).text
        values = random.sample(next(generated_value()).value, k=1)
        input_value = self.element_is_visible(self.locators.CLICK_SELECT_VALUE)
        for value in values:
            input_value.send_keys(value)
            time.sleep(0.2)
            input_value.send_keys(Keys.ENTER)
            time.sleep(0.2)
        return str(before), str(values)[1:-1:1]

    @allure.step('Выбор одного значения в работе с меню')
    def select_one(self):
        before = self.element_is_visible(self.locators.BEFORE_ONE).text
        one_value = random.sample(next(generated_one_value()).one_value, k=1)
        input_value = self.element_is_visible(self.locators.SELECT_ONE)
        for one in one_value:
            input_value.send_keys(one)
            time.sleep(0.2)
            input_value.send_keys(Keys.ENTER)
            time.sleep(0.2)
        return before, str(one_value)[1:-1:1]

    @allure.step('Старый стиль выбора меню')
    def old_style_select_menu(self):
        before_value = self.element_is_visible(self.locators.SELECT_MENU).get_attribute('value')
        self.element_is_visible(self.locators.SELECT_MENU).click()
        self.element_is_visible(self.locators.SELECT_MENU_VALUE).click()
        after_value = self.element_is_visible(self.locators.SELECT_MENU).get_attribute('value')
        return before_value, after_value

    @allure.step('Выпадающий список с несколькими вариантами выбора')
    def multiselect_drop_down(self):
        before_value = self.element_is_visible(self.locators.BEFORE_MULTI).text
        colors = random.sample(next(generated_four_color()).color_name, k=4)
        input_multi = self.element_is_visible(self.locators.MULTISELECT)
        for color in colors:
            input_multi.send_keys(Keys.ENTER)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)

        return before_value, colors







