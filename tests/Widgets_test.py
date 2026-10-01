from pages.Widgets_page import AccordianPage


class TestWidgetsPage:
    class TestAccordianPage:


        def test_check_text_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_text, second_text, third_text = accordian_page.check_accordian_text()
            assert first_text == 574
            assert second_text == 763
            assert third_text == 613


