import random

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.Widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
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