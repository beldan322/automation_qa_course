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

class RadioButtonPageLocators:

    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="form-check-label"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="form-check-label"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="form-check-label"][for="noRadio"]')
    OUTPUT_RADIOBUTTON = (By.CSS_SELECTOR, 'p span[class="text-success"]')

class WebTablePageLocators:

    # ADD NEW PERSON ON THE TABLE

    ADD_PERSON_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_PERSON = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE = (By.CSS_SELECTOR, "input[id='age']")
    SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_PERSON = (By.CSS_SELECTOR, "button[id='submit']")

    #CHECKING FOR ADDITIONS NEW PERSON

    CHEK_TABLE =(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/table/tbody')
    SEARCH_TABLE = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div[2]/table')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
