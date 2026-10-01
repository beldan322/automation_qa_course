from selenium.webdriver.common.by import By


class AccordianPageLocators:

    SECTION_FIRST = (By.XPATH, '//*[@id="accordianContainer"]/div/div[1]')
    SECTION_SECOND = (By.XPATH, '//*[@id="accordianContainer"]/div/div[2]')
    SECTION_THIRD = (By.XPATH, '//*[@id="accordianContainer"]/div/div[3]')
    SECTION_FIRST_TEXT = (By.XPATH, '//*[@id="accordianContainer"]/div/div[1]/div/div/p')
    SECTION_SECOND_TEXT = (By.XPATH, '//*[@id="accordianContainer"]/div/div[2]/div/div/p')
    SECTION_THIRD_TEXT = (By.XPATH, '//*[@id="accordianContainer"]/div/div[3]/div/div/p')
