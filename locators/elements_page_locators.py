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
class ButtonPageLocators:

    DOUBLE_CLICK = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    ONE_CLICK = (By.XPATH, '/html/body/div/div/div/div/div[2]/div[1]/div[3]/button')

    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    ONE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')

class LinksPageLocators:

    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")
    DINAMIC_LINK = (By.CSS_SELECTOR, "a[id='dynamicLink']")
    CREATED_LINK = (By.CSS_SELECTOR, "a[id='created']")
    NO_CONTENT_LINK = (By.CSS_SELECTOR, "a[id='no-content']")
    MOVED_LINK = (By.CSS_SELECTOR, "a[id='moved']")
    UNAUTHORIZET_LINK = (By.CSS_SELECTOR, "a[id='unauthorized']")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id='forbidden']")
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "a[id='invalid-url']")

    #response
    RESPONSE_LINK = (By.CSS_SELECTOR, "p[id='linkResponse']")

class UpLoadAndDownloadPageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOAD_RESULT = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")

class DynamicPropertiesLocators:
    ENABLE_AFTER = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_AFTER = (By.CSS_SELECTOR, "button[id='visibleAfter']")
