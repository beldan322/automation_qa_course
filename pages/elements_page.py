import time

from selenium.webdriver.common.by import By

from locators.elements_page_locators import RadioButtonPageLocators, WebTablePageLocators
from generator.generator import generated_person, generator_new_person
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



