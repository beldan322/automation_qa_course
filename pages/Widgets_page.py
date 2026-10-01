from locators.Widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()


    def check_accordian_text(self):
        self.element_is_visible(self.locators.SECTION_FIRST).click()
        first_text = self.element_is_present(self.locators.SECTION_FIRST_TEXT).text
        self.element_is_visible(self.locators.SECTION_SECOND).click()
        second_text = self.element_is_present(self.locators.SECTION_SECOND_TEXT).text
        self.element_is_visible(self.locators.SECTION_THIRD).click()
        third_text = self.element_is_present(self.locators.SECTION_THIRD_TEXT).text
        return len(first_text), len(second_text), len(third_text)
