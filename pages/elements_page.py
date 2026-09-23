import base64
import os
import random
import time


import pytest
import requests
from selenium.common import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By

from locators.elements_page_locators import RadioButtonPageLocators, WebTablePageLocators, ButtonPageLocators, \
    LinksPageLocators, UpLoadAndDownloadPageLocators, DynamicPropertiesLocators, PracticeFormLocators
from generator.generator import generated_person, generator_new_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()


    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANET_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_fields_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANET_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()
    def click_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                  'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                  'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def out_put_result(self):
        return self.element_is_present(self.locators.OUTPUT_RADIOBUTTON).text

class WebTablePage(BasePage):
    locators = WebTablePageLocators()
    def add_new_person(self):
        count =1
        while count != 0:
            person_info = next(generator_new_person())
            first_name = person_info.first_name
            last_name =person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_PERSON_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_PERSON).send_keys(email)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_PERSON).click()
            count -=1
            return [str(first_name), str(last_name), str(age), str(email), str(salary), str(department)]

    def chek_new_person(self):
        tbody = self.elements_are_present(self.locators.CHEK_TABLE)
        data = []
        for item in tbody:
            rows = item.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if cells:
                    data.append([cell.text.strip() for cell in cells[:6]])
        return data


    def search_person_in_table(self, key_words):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_words)

    def get_table_rows(self):
        search_person = self.elements_are_present(self.locators.SEARCH_TABLE)
        data = []
        for item in search_person:
            rows = item.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if cells:
                    data.append([cell.text.strip() for cell in cells])
        return data

class ButtonPage(BasePage):
    locators = ButtonPageLocators()


    def double_click(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK))
        return self.check_clicked_on_the_buttons(self.locators.DOUBLE_CLICK_MESSAGE)


    def right_click(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK))
        return self.check_clicked_on_the_buttons(self.locators.RIGHT_CLICK_MESSAGE)

    def one_click(self):
        self.element_is_visible(self.locators.ONE_CLICK).click()
        return self.check_clicked_on_the_buttons(self.locators.ONE_CLICK_MESSAGE)

    def check_clicked_on_the_buttons(self, element):
        return self.element_is_present(element).text

class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code

    def check_bad_request_link(self):
        self.element_is_present(self.locators.BAD_REQUEST).click()
        text_broken_link = self.element_is_present(self.locators.RESPONSE_LINK).text
        return text_broken_link


    def check_dinamic_link(self):
        simple_link = self.element_is_visible(self.locators.DINAMIC_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return url, link_href
        else:
            return requests.status_codes

    def check_created_link(self,):
        self.element_is_present(self.locators.CREATED_LINK).click()
        text_click = self.element_is_present(self.locators.RESPONSE_LINK).text
        return text_click

    def check_no_content_link(self):
        self.element_is_present(self.locators.NO_CONTENT_LINK).click()
        text_click = self.element_is_present(self.locators.RESPONSE_LINK).text
        return text_click
    def check_unauthorized_link(self):
        self.element_is_present(self.locators.UNAUTHORIZET_LINK).click()
        text_click = self.element_is_present(self.locators.RESPONSE_LINK).text
        return text_click

    def check_forbidden_link(self):
        self.element_is_present(self.locators.FORBIDDEN_LINK).click()
        text_click = self.element_is_present(self.locators.RESPONSE_LINK).text
        return text_click

    def check_not_found_link(self):
        self.element_is_present(self.locators.NOT_FOUND_LINK).click()
        text_click = self.element_is_present(self.locators.RESPONSE_LINK).text
        return text_click


class UpLoadAndDownloadPage(BasePage):
    locators = UpLoadAndDownloadPageLocators

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_clickable(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOAD_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\Users\belmas\PycharmProjects\automation_qa_course\filetest{random.randint(10, 100)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file

class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()

    def check_change_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_visible_botton(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER)
        except TimeoutException:
            return False
        return True

    def check_clickable_botton(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER).click()
        except ElementNotInteractableException:
            return False
        return True


