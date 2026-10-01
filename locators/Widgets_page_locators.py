from selenium.webdriver.common.by import By


class AccordianPageLocators:

    SECTION_FIRST = (By.XPATH, '//*[@id="accordianContainer"]/div/div[1]')
    SECTION_SECOND = (By.XPATH, '//*[@id="accordianContainer"]/div/div[2]')
    SECTION_THIRD = (By.XPATH, '//*[@id="accordianContainer"]/div/div[3]')
    SECTION_FIRST_TEXT = (By.XPATH, '//*[@id="accordianContainer"]/div/div[1]/div/div/p')
    SECTION_SECOND_TEXT = (By.XPATH, '//*[@id="accordianContainer"]/div/div[2]/div/div/p')
    SECTION_THIRD_TEXT = (By.XPATH, '//*[@id="accordianContainer"]/div/div[3]/div/div/p')


class AutoCompletePageLocators:

        MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
        MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__multi-value__label css-9jq23d"]')
        DELETE_MULTI_VALUE = (By.CSS_SELECTOR, "div[role='button']")
        SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
        SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1dimb5e-singleValue"]')
