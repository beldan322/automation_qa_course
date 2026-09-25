from selenium.webdriver.common.by import By
import random

class PracticeFormLocators:
    FIRST_NAME_FORM = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_FORM = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_FORM = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"input[id='gender-radio-{random.randint(1,3)}']")
    NUMBER_FORM = (By.CSS_SELECTOR, "input[id='userNumber']")
    BIRTH_DATE_FORM = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECT_FORM = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES_FORM = (By.CSS_SELECTOR, f"input[id='hobbies-checkbox-{random.randint(1,3)}']")
    PASTE_FILE_FORM = (By.XPATH, "//*[@id='uploadPicture']")
    CURRENT_ADDRESS_FORM = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SUBMIT_BUTTON_FORM = (By.CSS_SELECTOR, "button[id='submit']")
    CLOSE_BUTTON_FORM = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
    REGISTRATION_FORM = (By.XPATH, "//div[@class='table-responsive']//td[2]")
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    SELECT_STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
