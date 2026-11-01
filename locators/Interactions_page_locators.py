from selenium.webdriver.common.by import By


class SortablePageLocators:

    TAB_LIST = (By.CSS_SELECTOR, "div[id='demo-tabpane-list']")

    LIST_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")

    TAB_GRID = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid']")

    GRID_ITEM =(By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")

    BUTTON_LIST = (By.CSS_SELECTOR, 'button[id="demo-tab-list"]')

    BUTTON_GRID = (By.CSS_SELECTOR, 'button[id="demo-tab-grid"]')


class SelectablePageLocators:
        BUTTON_LIST = (By.CSS_SELECTOR, 'button[id="demo-tab-list"]')
        BUTTON_GRID = (By.CSS_SELECTOR, 'button[id="demo-tab-grid"]')

        TAB_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"]')
        TAB_GRID = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"]')

        LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
        LIST_GRID = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')

        ACTIVE_ITEM_LIST = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')
        ACTIVE_ITEM_GRID = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')