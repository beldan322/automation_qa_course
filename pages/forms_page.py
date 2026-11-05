import os
import time

import allure
import pytest
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from locators.forms_page_locators import PracticeFormLocators
from generator.generator import generator_new_person, generated_file
from pages.base_page import BasePage








class PracticeFormPage(BasePage):
    locators = PracticeFormLocators()

    @allure.step('Заполнение всех полей в форме регистрации')
    def fill_form_fields(self):
        person = next(generator_new_person())
        file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME_FORM).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME_FORM).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_FORM).send_keys(person.email)
        gender = self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.NUMBER_FORM).send_keys(person.mobile)
        subject = self.element_is_visible(self.locators.SUBJECT_FORM).send_keys('Maths')
        self.element_is_visible(self.locators.SUBJECT_FORM).send_keys(Keys.RETURN)
        hobbies= self.element_is_visible(self.locators.HOBBIES_FORM).click()
        self.element_is_present(self.locators.PASTE_FILE_FORM).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_FORM).send_keys(person.current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.SELECT_STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.SELECT_CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON_FORM).click()
        return person.first_name, person.last_name, person.email, person.mobile, gender, subject, hobbies, file_name, person.current_address

    @allure.step('Проверка заполненной формы')
    def check_created_form(self):
        student_form = self.elements_are_present(self.locators.REGISTRATION_FORM)
        data = []
        for item in student_form:
            self.go_to_element(item)
            data.append(item.text)
        return data




