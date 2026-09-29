from selenium.webdriver.common.by import By

class BrowserWindowsLocators:


    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    WORD_NEW_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, "button[id='messageWindowButton']")



class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFORM_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    RESULT_PROMPT = (By.CSS_SELECTOR, 'span[id="promptResult"]')





class FramesPageLocators:

    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class NestedFramePageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    TEXT_PARENT_FRAME = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    TEXT_CHILD_FRAME = (By.CSS_SELECTOR, 'p')


class ModalDialogsPageLocators:
    SMALL_MODAL = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')
    SMALL_MODAL_BODY = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    SMALL_CLOSE_BUTTON =(By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    LARGE_MODAL = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')
    LARGE_MODAL_BODY = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    LARGE_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')



