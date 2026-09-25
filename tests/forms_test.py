import random
import time
from pages.forms_page import PracticeFormPage


class TestForm:
    class TestPracticeFormPage:

        def test_form(self, driver):
            form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            created_student = form_page.fill_form_fields()
            check_student = form_page.check_created_form()
            print(created_student)
            print(check_student)
            # assert created_student == check_student



