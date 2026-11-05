import random
import time

import allure

from pages.forms_page import PracticeFormPage

@allure.suite('Группа "Forms"')
class TestForm:

    @allure.feature('Подгруппа "Practice Form"')
    class TestPracticeFormPage:

        @allure.title('Тест "Filling out the form"')
        def test_form(self, driver):
            form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            created_student = form_page.fill_form_fields()
            check_student = form_page.check_created_form()
            print(created_student)
            print(check_student)
            assert created_student == check_student



