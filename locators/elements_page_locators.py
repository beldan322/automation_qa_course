from selenium.webdriver.common.by import By


class TextBoxPageLocators:

#FROM FIELDS


    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL =  (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANET_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")



#FROM CREATED

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANET_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
