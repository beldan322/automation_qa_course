import os
import time

import allure
import pytest


from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert

from generator.generator import generated_person
from locators.Alerts_Frame_Windows_page_Locators import BrowserWindowsLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramePageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators()

    @allure.step('Открытие новой вкладки')
    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_text = self.element_is_present(self.locators.WORD_NEW_TAB).text
        if title_text == 'This is a sample page':
            return True
        else:
            return False

    @allure.step('Открытие нового окна')
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_new_window = self.element_is_present(self.locators.WORD_NEW_TAB).text
        return text_new_window


class AlertsPage(BasePage):
    locators = AlertsPageLocators

    @allure.step('Проверка алерта')
    def check_see_alert(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_text = self.driver.switch_to.alert
        return alert_text.text

    @allure.step('Проверка алерта спустя 5 сек')
    def check_alert_after_five_second(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        alert = self.alert_is_present()
        return alert.text

    @allure.step('Проверка алерта с подтверждением')
    def check_alert_confirm_text(self):
        self.element_is_visible(self.locators.CONFORM_ALERT_BUTTON).click()
        alert = self.alert_is_present()
        return alert.text

    @allure.step('Проверка алерта с подтверждением нажав на YES')
    def check_alert_confirm_button_yes(self):
        self.element_is_visible(self.locators.CONFORM_ALERT_BUTTON).click()
        alert = self.alert_is_present()
        try:
            return alert.text
        finally:
            alert.accept()

    @allure.step('Проверка алерта с подтверждением нажав на NO')
    def check_alert_confirm_button_no(self):
        self.element_is_visible(self.locators.CONFORM_ALERT_BUTTON).click()
        alert = self.alert_is_present()
        try:
            return alert.text
        finally:
            alert.dismiss()

    @allure.step('Проверка алерта с вводом')
    def check_prompt_alert(self):
        name = next(generated_person())
        full_name = name.full_name
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert = self.alert_is_present()
        alert.send_keys(full_name)
        alert.accept()
        text_form = self.element_is_visible(self.locators.RESULT_PROMPT).text
        try:
            return full_name
        finally:
            if full_name in text_form:
                return True




class FramesPage(BasePage):

    locators = FramesPageLocators()

    @allure.step('Проверка рамки')
    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            return [text, width, height]



class NestedFramePage(BasePage):
    locators = NestedFramePageLocators()

    @allure.step('Проверка вложенной рамки')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.TEXT_PARENT_FRAME).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.TEXT_CHILD_FRAME).text
        return parent_text, child_text



class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators

    @allure.step('Проверка простого модального окна')
    def check_simple_modal_dialog(self):
        self.element_is_visible(self.locators.SMALL_MODAL).click()
        text1 = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        text2 = self.element_is_visible(self.locators.SMALL_MODAL_BODY).text
        try:
            return text1, text2
        finally:
            self.element_is_visible(self.locators.SMALL_CLOSE_BUTTON).click()

    @allure.step('Проверка большого модального окна')
    def check_large_modal_dialog(self):
        self.element_is_visible(self.locators.LARGE_MODAL).click()
        text1 = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        text2 = self.element_is_visible(self.locators.LARGE_MODAL_BODY).text
        try:
            return text1, text2
        finally:
            self.element_is_visible(self.locators.LARGE_CLOSE_BUTTON).click()


















