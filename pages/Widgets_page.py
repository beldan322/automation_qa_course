import random
import time
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date, generated_time
from locators.Widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()


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

    def fill_multi_input(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
        for color in colors:
            input_multi.send_keys(Keys.ENTER) #работает и пофиг, я полчаса убил на решение проблемы, без энтера вначале он скипал цвета и даже увеличение таймаута в basepage не помогло
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors


    def delete_multi_color(self):
        before_value = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.DELETE_MULTI_VALUE)
        for value in remove_button_list:
            value.click()
            break
        after_value = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return before_value, after_value


    def check_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors=[]
        for color in color_list:
            colors.append(color.text)
        return colors


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


    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)


    def select_day_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for i in item_list:
            if i.text ==  value:
                i.click()
                break


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
