import os
import time
import pytest


from selenium.webdriver.common.by import By

from locators.Alerts_Frame_WindowsLocators import BrowserWindowsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsLocators()
    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_text = self.element_is_present(self.locators.WORD_NEW_TAB).text
        if title_text == 'This is a sample page':
            return True
        else:
            return False


    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_new_window = self.element_is_present(self.locators.WORD_NEW_TAB).text
        return text_new_window
